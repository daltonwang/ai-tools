#### IMDB-WIKI – 500k+ face images with age and gender labels
To the best of our knowledge this is the largest publicly available dataset of face images with gender and age labels for training. We provide pretrained models for both age and gender prediction.

##### 1. Description
Since the publicly available face image datasets are often of small to medium size, rarely exceeding tens of thousands of images, and often without age information we decided to collect a large dataset of celebrities. For this purpose, we took the list of the most popular 100,000 actors as listed on the IMDb website and (automatically) crawled from their profiles date of birth, name, gender and all images related to that person. Additionally we crawled all profile images from pages of people from Wikipedia with the same meta information. We removed the images without timestamp (the date when the photo was taken). Assuming that the images with single faces are likely to show the actor and that the timestamp and date of birth are correct, we were able to assign to each such image the biological (real) age. Of course, we can not vouch for the accuracy of the assigned age information. Besides wrong timestamps, many images are stills from movies - movies that can have extended production times. In total we obtained 460,723 face images from 20,284 celebrities from IMDb and 62,328 from Wikipedia, thus 523,051 in total.
As some of the images (especially from IMDb) contain several people we only use the photos where the second strongest face detection is below a threshold. For the network to be equally discriminative for all ages, we equalize the age distribution for training. For more details please the see the paper.

##### 2. Usage
For both the IMDb and Wikipedia images we provide a separate .mat file which can be loaded with Matlab containing all the meta information. The format is as follows:
- dob: date of birth (Matlab serial date number)
- photo_taken: year when the photo was taken
- full_path: path to file
- gender: 0 for female and 1 for male, NaN if unknown
- name: name of the celebrity
- face_location: location of the face. To crop the face in Matlab run
- img(face_location(2):face_location(4),face_location(1):face_location(3),:))
- face_score: detector score (the higher the better). Inf implies that no face was found in the image and the face_location then just returns the entire image
- second_face_score: detector score of the face with the second highest score. This is useful to ignore images with more than one face. second_face_score is NaN if no second face was detected.
- celeb_names (IMDB only): list of all celebrity names
- celeb_id (IMDB only): index of celebrity name
- The age of a person can be calculated based on the date of birth and the time when the photo was taken (note that we assume that the photo was taken in the middle of the year):
[age,~]=datevec(datenum(wiki.photo_taken,7,1)-wiki.dob); 

##### 3. Data Set
###### 3.1 IMDB images and metadata
https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/static/imdb_0.tar
https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/static/imdb_1.tar
https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/static/imdb_2.tar
https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/static/imdb_3.tar
https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/static/imdb_4.tar
https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/static/imdb_5.tar
https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/static/imdb_6.tar
https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/static/imdb_7.tar
https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/static/imdb_8.tar
https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/static/imdb_9.tar
https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/static/imdb_meta.tar
https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/static/imdb_crop.tar

###### 3.2 WIKI Data Set
https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/static/wiki.tar.gz
https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/static/wiki_crop.tar
https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/static/extractSubImage.m

##### 4. Model
##### 4.1 Real age estimation trained on IMDB-WIKI
https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/static/dex_imdb_wiki.caffemodel
https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/static/age.prototxt
https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/static/age_train.prototxt

##### 4.2 Apparent age estimation trained on LAP dataset
https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/static/dex_chalearn_iccv2015.caffemodel
https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/static/age.prototxt
https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/static/age_train.prototxt

##### 4.3 Gender prediction
https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/static/gender.caffemodel
https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/static/gender.prototxt
https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/static/gender_train.prototxt