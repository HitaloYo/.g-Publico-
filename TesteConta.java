public class TesteConta{
    public static void main(String[] args) {
        Conta minhaConta = new Conta("Fulano", 123, "001", 1000.0); // Criando uma instância da classe Conta
    }
    public static void main(String[] args) {
        Conta minhaConta2 = new Conta("Fulano", 123, "001", 1000.0); // Criando uma instância da classe Conta
    }

    if(minhaConta == minhaConta2){
        System.out.println("iguais");
    }else{
        System.out.println("diferentes");
    }
    
    
}
