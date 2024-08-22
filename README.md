# Librería de Computación Cuántica
Este proyecto incluye una librería para realizar operaciones con números complejos, facilitando su manejo y acelerando los cálculos relacionados con ellos.

### Para utilizar esta librería, necesitas:
- Python: Un intérprete de Python 3.8 o superior. Puedes descargarlo desde [python.org](https://www.python.org/).
- Editor de Código: Todo el código fuente fue implementado en el editor VSCO (Visual Studio Code), no obstante puedes utilizar cualquier editor de código que sea de tu preferencia.
  
# Estructura del proyecto:
El proyecto esta dividido en dos fases: 
- **Operaciones**:
    En esta sección podras encontrar las operaciones básicas entre números complejos como lo son:
  
    - SUMA
    - MULTIPLICACIÓN
    - DIVISIÓN
      
    Y tambien encontraras operaciones con un poco más de complejidad como lo son:
  
    - MODULO
    - PASAR DE COORDENADAS CARTESIANAS A COORDENADAS POLARES
    - PASAR DE COORDENADAS POLARES A CARTESIANAS
    - HALLAR LA FASE
      
- **Pruebas**: En esta sección encontraras todas la pruebas que verifican la funcionalidad de los programas.

# Ejemplo de uso:

### Ejemplo de Uso

  
  Podemos observar la implementacion del 'algoritmo' para poder dividir dos números complejos, en la cual la vamos a dividir en dos:
  1. Vamos a encontrar la parte real del número.
  2. Vamos a encontrar la parte imaginaria dl número.
    
    
         def dividirComplejos(a, b):
      
          real = (a[0]*b[0] + a[1]*b[1]) / (b[0]**2 + b[1]**2)
          imaginaria = (a[1]*b[0] - a[0]*b[1]) / (b[0]**2 + b[1]**2)
          return real, imaginaria
      
          def prettyPrinting(r):
            print(r[0],'+', r[1],'i')
        
          if __name__ == "__main__":
            prettyPrinting(dividirComplejos([-3,1],[1,3]))

            
## Construido con:

- **Python**: El lenguaje de programación utilizado para realizar las operaciones entre números complejos.
- **Visual Studio**: Entorno de desarrollo integrado utilizado para el desarrollo del proyecto.
## Autor

- **Sergio Alejandro Idarraga**: Desarrollador principal del proyecto.
