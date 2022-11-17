Funciones
=========


Esta es una herramienta que solo se ejecuta en consola, conminima interacción

Para ello tenemos diversos parametros

``-ty``: es el tipo de scaneno que vamos a hacer, las opciones son: [*file*, *link*, *image*, *ip*, *pdf*, *process*]

``-InRo``: es el nombre de lo que vamos a scanear

``-OuRo``: es el nombre **solo el nombre** del archivo donde guardaremos el resultado si no se ingresa esta opcion el resultado se imprimira en la consola

``-OuFi``: es la extencion del archivo donde guardaremos el resultado, las opciones: [*.txt*, *.json*, *print*] si no se ingresa esta opcion el resultado se guardara en un .json

``-key``: es tu llave para poder usar la api de virus total


ScanearporVirus
---------------

Si lo que quieres es comprobar que un archivo no tenga virus usa: 

.. py:function:: scan_files.scan_files(archivo, key)

    
    Nos da el estado de un archivo.
    Para usar esta funcion es necesario tener una llave de virustotal


    Puedes ejecutarlo con el siguiente comando:

    `$ py scaneador.py -ty file -InRo [archivo] -OuRo [nombre] -OuFi [extencion] -key [tu_llave]`

    
    :param archivo: Obligatorio el nombre del archivo a scanear
    :type archivo: String
    :param key: Obligatorio tu llave para la API de virustotal
    :type key: String
    :return: la informacion encontrada
    :rtype: json


Si lo que quieres es comprobar que un link no tenga virus usa:

.. py:function:: scan_links.scanlink(link, key)
    

    Nos da el estado de un link.
    Para usar esta funcion es necesario tener una llave de virustotal


    Puedes ejecutarlo con el siguiente comando:

    `$ py scaneador.py -ty link -InRo [link] -OuRo [nombre] -OuFi [extencion] -key [tu_llave]`


    :param link: Obligatorio el link a scanear
    :type link: String
    :param key: Obligatorio tu llave para la API de virustotal
    :type key: String
    :return: la informacion encontrada
    :rtype: json


ScanearPdfs
-----------

Si lo que quieres es comprobar la metadata de un archivo pdf usa:

.. py:function:: scan_pdf.scanpdf(archivo)
    

    Nos da un diccionario con la metadata encontrada del archivo


    Puedes ejecutarlo con el siguiente comando:

    `$ py scaneador.py -ty pdf -InRo [archivo] -OuRo [nombre] -OuFi [extencion]`


    :param archivo: Obligatorio el nombre del pdf a scanear
    :type archivo: String
    :return: un diccionario con la metadata encontrada del archivo
    :rtype: diccionario


ScanearImagenes
---------------

Si lo que quieres es comprobar la metadata de una imagen usa:

.. py:function:: scan_img.scan_image(imagen)
    
    Nos da la metadata encontrada de la imagen


    Puedes ejecutarlo con el siguiente comando:

    `$ py scaneador.py -ty image -InRo [imagen] -OuRo [nombre] -OuFi [extencion]`


    :param imagen: Obligatorio el nombre de la imagen a scanear
    :type imagen: String
    :return: a metadata encontrada de la imagen
    :rtype: lista


ScanearIps
----------

Si lo que quieres es comprobar el estado de una IP usa:

.. py:function:: scan_ip.scan_ip(host)
    
    Nos comprueba el estado de una IP


    Puedes ejecutarlo con el siguiente comando:

    `$ py scaneador.py -ty ip -InRo [host] -OuRo [nombre] -OuFi [extencion]`


    :param host: Obligatorio direccion IP
    :type host: String
    :return: archivo con los datos encontrados


ScanearProceso
--------------

Si lo que quieres es comprobar los procesos usa:

.. py:function:: scan_process.all_process()
    
    Nos da el estado de todos los procesos


    Puedes ejecutarlo con el siguiente comando:

    `$ py scaneador.py -ty process -InRo all -OuRo [nombre] -OuFi [extencion]`


    :return: la informacion de los procesos


Si lo que quieres es comprobar un solo proceso usa:

.. py:function:: scan_process.single_process(name)
    
    Nos da el estado de un proceso especificado


    Puedes ejecutarlo con el siguiente comando:

    `$ py scaneador.py -ty pdf -InRo [name] -OuRo [nombre] -OuFi [extencion]`


    :param name: Obligatorio nombre del proceso a comprobar
    :type name: String
    :return: la informacion del procesos



Errores
=======

Si algun error llega a ocurrir durante la ejecución, 
se vera en la panalla una notificación de error y se creara un archivo llamado **error.log**
donde se guardara el registro del error