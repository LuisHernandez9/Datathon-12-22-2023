import os
from deepface import DeepFace

#function definitons for main
#filename
def filename(img_loc):
    path = img_loc
    img_name = os.listdir(path)
    return img_name

#gender analysis
def gender(img):
    try:
        output = DeepFace.analyze(img, actions=['gender'])
        return output[0]['gender']
    except:
        return 'Unknown'

#ethnicity analysis
def ethnicity(img):
    try:
        output = DeepFace.analyze(img, actions=['race'])
        return output[0]['race']
    except:
        return 'Unknown'

#age analysis
def age(img):
    try:
        output = DeepFace.analyze(img, actions=['age'])
        return output[0]['age']
    except:
        return '-1'

#output results in a csv file
def csv(results):
    with open ('Analysis_Results.csv','w') as l:
        l.write('Filename, Gender, Ethnicity, Age\n')
        for value in results.items():
            filename = value[0].split('\\')[1]
            age = value[1]['Age']
            try:
                ethnicity = max(value[1]['race'], key=value[1]['race'].get)
            except:
                ethnicity = "Unknown"
            try:
                gender = max(value[1]['Gender'], key=value[1]['Gender'].get)
            except:
                gender = "Unknown"

            l.write(f'{filename},{gender},{ethnicity},{age}\n')

#main function            
def main(img_loc = 'faceimages'):
    image_files = os.listdir(img_loc)
    image_files=[x for x in image_files if x.endswith('png')]
    results={}
    
    for img in image_files:
        img = os.path.join(img_loc, img)
        genderi = gender(img)
        ethnicityi = ethnicity(img)
        agei = age(img)
        results[img] = {'Gender':genderi,'race':ethnicityi,'Age':agei}
    csv(results)


if __name__=='__main__':
    main()
