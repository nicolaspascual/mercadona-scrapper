# Mercadona Scrapper

Repository that using selenium web driver downloads all catalogue of products from
mercadona website including price, name and link to the product.  

## Running the code

In order to start the scrapper you need to enter your credentials of mercadona in
`/conf/credentials.py` and run the main file. This will generate a csv file with
the products.

## Results 

The results will look as follows:

| title                                                                                  | link                                                             | price |
|----------------------------------------------------------------------------------------|------------------------------------------------------------------|-------|
| ABADEJO ALASKA CONGELADO FILETE (SIN PIEL), MASCATO, PAQUETE 850 G PESO NETO ESCURRIDO | https://www.telecompra.mercadona.es/detall_producte.php?id=62180 | 4.95  |
| ABRILLANTADOR LAVAVAJILLAS, , BOTELLA 750 CC                                           | https://www.telecompra.mercadona.es/detall_producte.php?id=42306 | 1.25  |
| ABRILLANTADOR LAVAVAJILLAS, FINISH CALGONIT, BOTELLA 500 CC                            | https://www.telecompra.mercadona.es/detall_producte.php?id=42301 | 4.45  |
|                                                                                ............                                                                       |
| ABRILLANTADOR SUELO, BOSQUE VERDE, BOTELLA 1 L                                         | https://www.telecompra.mercadona.es/detall_producte.php?id=43375 | 2.05  |
| ACEITE ANTIOXIDANTE MULTIUSOS SPRAY, BOSQUE VERDE, BOTE 200 CC                         | https://www.telecompra.mercadona.es/detall_producte.php?id=90404 | 1.95  |

## Dependencies

The file uses pipenv to manage the dependencies, all dependencies can be found in
`/Pipfile`


```
              (
               )
              (
        /\  .-"""-.  /\
       //\\/  ,,,  \//\\
       |/\| ,;;;;;, |/\|
       //\\\;-"""-;///\\
      //  \/   .   \/  \\
     (| ,-_| \ | / |_-, |)
       //`__\.-.-./__`\\
      // /.-(() ())-.\ \\
     (\ |)   '---'   (| /)
      ` (|           |) `
        \)           (/
```