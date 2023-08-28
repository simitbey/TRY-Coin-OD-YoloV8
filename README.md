
# Object Detection - TRY Coins Model and Script

This project is as a proof-of-concept for an Object detection project. As a starting point, I used generic turkish coins with a model consisting of 80 images. More information of models on `/models/models.md`



## Deployment
### Google Colab
```bash
!pip install ultralytics
```
then add the `main.py` as a code, upload the model of your choice to `/content` and also the specified image with the name `input_image.jpg`.

### Local Machine
```
pip install ultralytics
```
then add the `main.py` and the model of your choice in the directory. upload the specified image with the name `input_image.jpg`. Run the code.




## Screenshots

Example was tested on Google Colab with the `TR-Coin-OD-v1` model.

![App Screenshot](https://cdn.discordapp.com/attachments/934317532276486255/1145639917259587695/image.png)

## Roadmap

- New v2 model with 500+ images trained as a dataset.

- A mobile app written with `js`.


## License


[MIT](https://choosealicense.com/licenses/mit/) License


Copyright (c) 2023 Alfa Ozaltin

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

