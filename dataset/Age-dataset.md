## **1. IMDB-WIKI数据集**
###  Description
论文作者分享了IMDB-WIKI数据集，包含524230张从IMDB 和Wikipedia爬取的名人数据图片。作者列出了IMDb网站上列出的最受欢迎的100,000名演员名单，并（自动）从他们的个人资料中抓取出生日期，姓名，性别以及与该人相关的所有图像。此外，作者使用相同的元信息从维基百科的人物页面中抓取所有个人资料图像。作者删除了没有时间戳的图像（拍摄照片的日期），假设演员拍摄图片的时间戳和出生日期是正确的，就能够计算出每张图片的真实年龄。当然，从网络上获取的图像无法保证指定年龄信息的准确性。作者总共获得了来自IMDb的20,284位名人的460,723张面部图像和来自维基百科的62,328张图像，共计523,051张。
- 为了使网络对所有年龄段具有同等的辨别力，作者均衡了训练集年龄分布。
### How to use it
对于IMDb和维基百科图像，我们提供了一个单独的.mat文件，可以使用Matlab加载。格式如下：
- **dob:** date of birth (Matlab serial date number) 
- **photo_taken:** year when the photo was taken 
- **full_path:** path to file
- **gender:** 0 for female and 1 for male, *NaN* if unknown 
- **name:** name of the celebrity   
- **face_location:** location of the face. To crop the face in Matlab run 
- **face_score:** detector score (the higher the better). Inf implies that no face was found in the image and the face_location then just returns the entire image 
- **second_face_score:**  detector score of the face with the second highest score. This is useful to ignore images with more than one face. second_face_score is NaN if no second face was detected.
- **celeb_names (IMDB only):** list of all celebrity names 
- **celeb_id (IMDB only):** index of celebrity name
The age of a person can be calculated based on the date of birth and the time when the photo was taken (note that we assume that the photo was taken in the middle of the year):

图片中的名人年龄可以通过下面的公式进行计算。

```
[age,~]=datevec(datenum(wiki.photo_taken,7,1)-wiki.dob); 
```
### Download
https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/
### Related Paper
https://www.vision.ee.ethz.ch/en/publications/papers/proceedings/eth_biwi_01229.pdf




## 2.MegaAge/MegaAge-Asian (2017)
###  Description
MegaAge数据集由商汤发布，总数有41941张图片，同一论文提出的MegaAge-Asian包含40000张亚洲人（绝大部分是东亚人）的图片，两个数据集年龄段都是0-70。数据集人脸的原始来源是MegaFace和YFCC。论文中提到，由于MegaAge-Asian的种族相对单一，故同一年龄估计算法MegaAge-Asian上的表现一般要优于MegaAge数据集上的表现。经观察，MegaAge-Asian标注结果比较精准，提供的图片大小统一为178*218，在保持比例前提下进行了补边操作，数据集包含了明星和普通人的图片。 
### Download
- http://mmlab.ie.cuhk.edu.hk/projects/MegaAge/
### Related Paper
- http://personal.ie.cuhk.edu.hk/~ccloy/files/bmvc_2017_megaage.pdf


## 3. AGE-DB（2017）
###  Description
AgeDB包含16,488个各种名人的图像，如演员，作家，科学家，政治家，每个图像都注明了身份，年龄和性别属性。共存在568个不同的科目。 每个科目的平均图像数为29。最低和最高年龄分别为1和101。每个科目的平均年龄范围是50.3岁。
### Download
- https://ibug.doc.ic.ac.uk/resources/agedb/
### Related Paper
- https://core.ac.uk/download/pdf/83949017.pdf


##   4. AFAD (2016)
###  Description
数据集规模为164432张脸，其中63680张女性、100752男性。年龄段为15-40岁。该数据集的特点是数据几乎全是中国人。该数据的数据来源为人人网，首先爬取人人网上的图片数据并获取相册所有者的年龄，然后使用人力对错误图片进行过滤。本数据年龄分布也不是很均衡，在最年轻和年纪较大的年龄段数据较少（也好理解，因为该年龄使用人人网的人少）。根据观察，感觉数据集整体标注效果比较准确，但有一些小图片（22*22）看不清楚，且有很多同一个人的图片几乎完全一样。数据集还有一个特点就是图片截取的较小，只留了较少的脸部，发型和颈部都去除了。其实年龄估计和人的发型、身体等也有一定联系，截取太小将无法使用到这些信息。
### Download
- https://github.com/afad-dataset/tarball
### Related Paper
- https://www.cv-foundation.org/openaccess/content_cvpr_2016/papers/Niu_Ordinal_Regression_With_CVPR_2016_paper.pdf


## 5. ChaLearn LAP Dataset (2015 / 2016)
### Description
LAP（Look At People）竞赛于2015和2016举办了两年，两年数据集规模分别为5000和8000（基于官网）。与其他数据集的标签为真实年龄不同，LAP数据集的标签是外观显示年龄（apparent age），标签制定平均了至少10个人的标注结果，所以每张图片的年龄标签都是一个正态分布。比赛排名中使用的是结合均值和方差的综合误差E-error。LAP数据集在20-40岁的分布相对均匀，在0-15和65-100区间数据集较少。
### Download
- http://chalearnlap.cvc.uab.es/dataset/19/description/
### Related Paper
- http://www.cbsr.ia.ac.cn/users/jwan/papers/CVPRW2016_JunWan.pdf
