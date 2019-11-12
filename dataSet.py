import cv2
import os 

cascPath = "Cascades/haarcascade_frontalface_alt2.xml"

def entrenamiento():
    import numpy as np
    import pickle
    from PIL import Image
    
    faceCascade = cv2.CascadeClassifier(cascPath)
    reconocimiento = cv2.face.LBPHFaceRecognizer_create()

    #direccionamiento de imagenes
    direccion_base =os.path.dirname(os.path.abspath(__file__))
    direccion_de_imagenes = os.path.join(direccion_base,"images")
    
    #Declaracion de etiqueta de alumno a reconocer
    idActual=0;
    etiquetas_id = {}
    y_etiquetas = []
    x_entrenamiento = []
    
    for raiz,direccion,archivos in os.walk(direccion_de_imagenes):
        for archivo in archivos:
            #selecciona los archivos que terminen en png o jpg
            if archivo.endswith("png") or archivo.endswith("jpg"):
                direccion_imagen = os.path.join(raiz,archivo)
                etiqueta=os.path.basename(raiz).replace(" ","-").lower()
                
                print(etiqueta,direccion_imagen)
                
                #Se crean las etiquetas
                
                if not etiqueta in etiquetas_id:
                    etiquetas_id[etiqueta]=idActual
                    idActual=idActual+1
                _id_=etiquetas_id[etiqueta]
                print(etiquetas_id)
                
                pil_image=Image.open(direccion_imagen).convert("L")
                
                tamanyo=(550,550)
                imagen_final=pil_image.resize(tamanyo,Image.ANTIALIAS)
                array_imagen=np.array(pil_image,"uint8")
                
                #mostrar imagen final
                #cv2.imshow("imagen final",imagen_final)
                
                rostros = faceCascade.detectMultiScale(array_imagen, 1.5, 5)

                for (x,y,w,h) in rostros:
                    rol = array_imagen[y:y+h, x:x+w]
                    x_entrenamiento.append(rol)
                    y_etiquetas.append(_id_)


#print(y_etiquetas)                
#print(x_entrenamiento)
    with open("labels.pickle",'wb') as f:
        pickle.dump(etiquetas_id, f)

    reconocimiento.train(x_entrenamiento, np.array(y_etiquetas))
    reconocimiento.save("entrenamiento.yml")
    return    
    
def dataSet(name):
    captura=cv2.VideoCapture(0)

    cascPath = "Cascades/haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascPath)
   
    contador=1000;


    while(captura.isOpened()):
        _,imagen=captura.read()
    
        grises=cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)
    
    
        rostro=faceCascade.detectMultiScale(grises,1.5,5)
    
        if not os.path.exists("images/"+name):
            os.mkdir("images/"+name)
   
        for(x,y,w,h) in rostro:
       
            cv2.rectangle(imagen, (x,y), (x+w, y+h), (255,0,100), 2)
            contador=contador+1
            
            cv2.imwrite("images/"+name+"/"+name+"_"+str(contador)+".jpg",grises[y:y+h,x:x+w])
            cv2.imshow('Ingreso de Rsotro',imagen)
        if cv2.waitKey(1)& 0xFF==ord('s'):
            break
        elif contador>=10000:
            break
    
    captura.release()
    cv2.destroyAllWindows()
    
def reconocimiento():
    import pickle

    faceCascade = cv2.CascadeClassifier(cascPath)
    eyeCascade = cv2.CascadeClassifier("Cascades/haarcascade_eye.xml")
    smileCascade = cv2.CascadeClassifier("Cascades/haarcascade_smile.xml")
    
    reconocimiento = cv2.face.LBPHFaceRecognizer_create()
    reconocimiento.read("entrenamiento.yml")
    
    etiquetas = {"nombre_persona" : 1 }
    with open("labels.pickle",'rb') as f:
        pre_etiquetas = pickle.load(f)
        etiquetas = { v:k for k,v in pre_etiquetas.items()}
    
    web_cam = cv2.VideoCapture(0)
    
    while True:
        # Capture el marco
        ret, marco = web_cam.read()
        grises = cv2.cvtColor(marco, cv2.COLOR_BGR2GRAY)    
        rostros = faceCascade.detectMultiScale(grises, 1.5, 5)
    
        # Dibujar un rectángulo alrededor de las rostros
        for (x, y, w, h) in rostros:
            #print(x,y,w,h)
            roi_gray = grises[y:y+h, x:x+w]
            roi_color = marco[y:y+h, x:x+w]
    
            # reconocimiento
            id_, conf = reconocimiento.predict(roi_gray)
            if conf >= 4  and conf < 85:
                #print(id_)
                #print(etiquetas[id_])           
                font = cv2.FONT_HERSHEY_SIMPLEX            
    
                nombre = etiquetas[id_]
    
                #if conf > 50:
                    #print(conf)
                    #nombre = "Desconocido"
    
                color = (255,255,255)
                grosor = 2
                cv2.putText(marco, nombre, (x,y), font, 1, color, grosor, cv2.LINE_AA)
    
            img_item = "my-image.png"
            cv2.imwrite(img_item, roi_gray)
            
            cv2.rectangle(marco, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
            rasgos = smileCascade.detectMultiScale(roi_gray)
            for(ex,ey,ew,eh) in rasgos:
                cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
        
        # Display resize del marco  
        marco_display = cv2.resize(marco, (1200, 650), interpolation = cv2.INTER_CUBIC)
        cv2.imshow('Detectando Rostros', marco_display)
    
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Cuando todo está hecho, liberamos la captura
    web_cam.release()
    cv2.destroyAllWindows()
#dataSet("rousseau")
#entrenamiento()

#cv2.waitKey(5000)
reconocimiento();
    
