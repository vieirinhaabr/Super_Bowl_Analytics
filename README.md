# **Design Pattern Implementation**
Implementação de 3 design pattern's para o trabalho.
## **Factory**
A exemplo do ***factory***, foi implementado a ["property"](https://github.com/wandreuscv/design-pattern-implementation/tree/master/src/com/designpattern/property) usando este pattern, ficou escalável e simples de incluir novos tipos de propriedade, podendo ainda modificar os tipos dos parâmetros passados em sua construção, como foi o caso com **bedRoomsQuantity** e **mainRoomSize**:
```
Property property;

property =  new  House(propertySize, propertyValue, propertyType, bedRoomsQuantity);
property =  new  Building(propertySize, propertyValue, propertyType, mainRoomSize);
```

## **Bridge**
A exemplo do ***bridge***, foi implementado a ["tax"](https://github.com/wandreuscv/design-pattern-implementation/tree/master/src/com/designpattern/tax) usando este pattern. Usando o ***bridge*** foi possível separar classes que possuem dimensões/propósitos diferentes, no caso a do "valor da taxa de imposto" do imóvel de suas "características e dados":

<p align="center">
  <img width="500" height="250" style="align=center;" src="https://github.com/wandreuscv/design-pattern-implementation/blob/master/Temp/Diagrama_BRIDGE.png?raw=true">
</p>

## **Strategy**
A exemplo do ***strategy***, foi implementado a ["owner"](https://github.com/wandreuscv/design-pattern-implementation/tree/master/src/com/designpattern/owner) usando esse pattern. Usando este pattern, foi possível modificar o comportamento do programa de forma simples, tornando os objetos intercambiáveis:
```
// IMPLEMENTATION - Property Class

OwnerInterface owner;

@Override
public void setOwnerType(OwnerInterface owner) {
	this.owner = owner;
}

// CALLING - Main

if (insertion.nextBoolean()){
	property.setOwnerType(new Physical());
} else{
	property.setOwnerType(new Juridical());
}
```
 
## **Integrantes do Trabalho**

 - yagohsp = Yago Henrique dos Santos Pacheco
 - wandreuscv = Wandreus Caetano Vieira

>  Professor: FILIPE GUELBER MELO
>  Matéria: ANÁLISE E DESENVOLVIMENTO DE SISTEMAS
