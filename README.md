# 🚀 Box and Bag Detection with YOLO and Transfer Learning 🚀

In this project, I've used **transfer learning** to train a **YOLO** model, adapting it to more effectively detect boxes and bags. I noticed that the specific types of boxes in the provided images weren't being detected well by off-the-shelf models, so I focused on refining that.

---

## 💡 My Training Approach

For training the model, I used two of the three images provided to me. Given the small number of examples, I decided to **expand the dataset** by creating artificial backgrounds, performing rotations, and perturbing the images. The goal was to make the model more **robust** and capable of handling different scenarios.

Additionally, since I'm working with a **GTX 1050TI**, I reduced the image size to **640x640**. Leaving them at their original resolution might have, well, pushed my GPU a bit too hard! (maybe even explode)

---

## 👀 Model Evaluation

I used the last image as a way to evaluate the model. However, if you'd like to test it yourself, I've included a script in the repository called `probando_modelo.py`. Here's a look at the results:

As you can see, **almost all boxes and bags are detected**.

<img width="970" height="972" alt="image" src="https://github.com/user-attachments/assets/d08e9896-34a0-4e71-be2d-0955de32cb2f" />

---

## 🎯 Ideas for Improvement

A possible improvement would be to detect the **top face of the box or bag**. With some **linear algebra**, the **normal vector of the plane** formed by that face could be calculated, which would indicate the most favorable direction for a "pick" action.

---

## 🌱 My Journey and Future Projections

I know that my current solution doesn't fully cover the problem, as I haven't had the opportunity to advance as quickly on my own due to my current internship. Furthermore, I haven't finished my degree yet; I'm about to start my final year, where I'll be studying **perception systems**. To add to that, this year my Final Degree Project (TFG) is on cone detection with a stereo camera for the Formula Student AI competition, which focuses on autonomous driving. In October, I'll also be taking a **deep learning** course offered by **Deep Learning Institute of Nvidia** to enhance my knowledge, as everything I've shown here comes from a **machine learning** extracurricular course I took last academic year.

Seeing the problems presented made me realize how much more I have to learn. Therefore, I'd appreciate it if you'd consider me for **future positions or even internships**. Despite being from Málaga, I'm willing to **relocate to Barcelona** once I finish my degree to pursue these opportunities.

---

## Finally

By the way, would it be possible to know the solutions of the other participants? Even though I might not be able to contribute much to the solutions right now, I'd love to learn from others. Or, if you have the answers to the problems, that would be great too!

Thank you very much!
