# PS-Pet-adoption

## TODAS AS FUNCIONALIDADES FORAM IMPLEMENTADAS:
- Pet Profile Management;
- User Account Management;
- Search and Filter Options;
- Shelter and Rescue Organization Proles;
- Donation Processing;
- Community Forum;
- Educational Resources;
- Event Listing and Management;
- Success Stories and Testimonials.

## Creational Design Patterns
### Builder
Justificativa: antes esse arquivo possuia apenas uma única função grande responsável por todo o processo, o que dificultava o entendimento do código e a mudança dele caso necessário. Dessa forma, o Builder foi utilizado para facilitar o entendimento e modificação do código caso queira adicionar mais funções.
  
## Estrutural Design Patterns
### Facade
Neste projeto, foi aplicado o padrão de design estrutural Facade para simplificar a interação com o sistema de adoção de pets. A classe PetAdoptionFacade centraliza funcionalidades como:
  - Listar pets disponíveis para adoção;
  - Exibir informações detalhadas de um pet;
  - Iniciar o processo de adoção.
  
  Antes, essas operações estavam espalhadas por diferentes módulos, tornando o código mais difícil de manter e reutilizar. Com o Facade, criamos uma interface única e intuitiva, que encapsula a complexidade e   melhora a organização e legibilidade do sistema. Isso torna o código mais limpo, modular e fácil de estender.
