# Image Processing
## _Challenge for the selection process of intern at Tarken_
### Reference Image:
![meteor_challenge_01](https://user-images.githubusercontent.com/72756630/200418773-8363edbf-ed55-4f5c-811f-9527eeab1f6d.png)
### Challenges:
1. Count the number of Stars ✅
2. Count the number of Meteors ✅ 
3. If the Meteors are falling perpendicularly to the Ground (Water level), count how many will fall on the Water ✅ 
4. (optional) Find the phrase that is hidden in the dots in the sky. ❌

| Questionns | Answers |
| ------ | ------ |
| Number of Stars | 315 |
| Number of Meteors | 328 |
| Meteors falling on the Water | 105 |
| (optional) Hidden Phrase| null |

## How did I arrive at this result?

I used the OpenCV library and invert the colors of the image to have a greater contrast between the pixels <br>
I separated the color scales where the stars and meteors fit and I counted how many pixels were in that range of colors <BR><BR>
To know how many meteors will fall into the water I created a mask over the desired pixel colors and generated an image.png for debugging<br>
use the numpy library to find out which red pixel columns (meteors) meet with the blue pixel columns (water), generating an array with these values

