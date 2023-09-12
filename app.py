from fastapi import FastAPI, UploadFile, HTTPException, File
from PIL import Image
from torchvision import models, transforms
import torch
import io

app = FastAPI()

resnet = models.resnet50(pretrained=True)

def preprocessing(img: Image):
    preprocess = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(
            mean=[0.485, 0.456, 0.406],
            std=[0.229, 0.224, 0.225]
        )])
    return preprocess(img)

@app.post("/upload/")
async def upload_file(item: UploadFile = File(...)):
    try:
        image_data = await item.read()
        image = Image.open(io.BytesIO(image_data))
        image = preprocessing(image)
        label, confidence = classify_image(image)
        return {"label": label, "confidence": confidence}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Bad request: {str(e)}")

@app.post("/classify/")
def classify_image(image):
    try:
        batch_t = torch.unsqueeze(image, 0)
        resnet.eval()
        out = resnet(batch_t)

        _, index = torch.max(out, 1)

        percentage = torch.nn.functional.softmax(out, dim=1)[0] * 100

        with open("imagenet_classes.txt") as f:
            labels = [line.strip() for line in f.readlines()]

        return labels[index[0]], percentage[index[0]].item()
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Classification error: {str(e)}")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)






