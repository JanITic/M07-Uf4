# PRÀCTICA 1 - VIEWS I TEMPLATES


1. Crear un projecte de DJANGO de nom TIC_GestioPersonal.
El nom de l’aplicació a on s’hi afegiran els templates i les views és centre.
Es farà una aplicació per mostrar dades de l’alumnat de DAW2B i del seu professorat.
Dades a mostrar alumnat: nom, cognom1, cognom2, correu, curs, mòduls matriculats.
Dades a mostrar prof.: nom, cognom1, cognom2, correu, curs, tutor(si s’escau),mòduls que imparteix.

   - Path alumne: localhost:8000/centre/students
   - Path professor: localhost:8000/centre/teachers

    Només la pàgina principal (del projecte) ha de renderitzar també un header. Aquest header sempre es mostrarà (independentment de si està mostrant dades de professorat o d’alumnat).

# PRÀCTICA 2 - CRUD
## BASES DE DADES

Trieu el tipus de bases de dades que vulgueu utilitzar en aquesta pràctica.  
Haureu de crear una bases de dades amb el nom `iticBCN`.  
Haureu de crear mínim una taula:  

- **usuari**: id, nom, cognom, assignatures, rol.  

En el cas de ser professor haurem de saber les assignatures que està impartint.  
Fer servir mínim una taula relacional per gestionar els rols i relacionar-ho amb la taula usuari. (1 punt)  

- **Taula rol**: id, nom.  
  - Ex: 1, professor

## CRUD

A partir de la pràctica anterior on feiem servir fakedata, haurem de fer els canvis necessaris per crear un CRUD de professors i estudiants que utilitzi les bases de dades definida en l’apartat anterior.

Feu els canvis necessaris en l’aplicació per gestionar un CRUD per professors i alumnes:

- **READ** (2 punts)
- **CREATE** (3 punts)
- **UPDATE** (3 punts)
- **DELETE** (1 punt)

Cada vegada que es fa un create, update o delete, les dades que apareixin a la vista després del CRUD estaran actualitzades.

Les pàgines de formularis s’han de crear amb el `forms.py` (segons explicació diapositives de form).
