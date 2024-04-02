public class TesteConta{
    public static void main(String[] args) {
        Conta minhaConta = new Conta("Fulano", 123, "001", 1000.0); // Criando uma instância da classe Conta
        Conta minhaConta2 = new Conta("Fulano", 123, "001", 1000.0);
        
        if (minhaConta == minhaConta2) { //Sempre será falso pois apesar de terem atributos iguais são objt diferenstes
            System.out.println("iguais");
        } else {
            System.out.println("diferentes");
        }
    }

    
    
}
