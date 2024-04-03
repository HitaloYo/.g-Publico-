public class Conta{
    private String titular;
    private int numero;
    private String agencia;
    private double saldo;
    Data dataDeAbertura;
    
//construtor
public Conta(String titular, int numero, String agencia, double saldo, Data dataDeAbertura){
   this.titular = titular;
   this.numero = numero;
   this.agencia = agencia;
   this.saldo = saldo;
}
    
    public void saca(double valor){
      if (valor <= saldo){
          this.saldo -= valor;
      }  
    }
    
    public void deposita(double valor){
        this.saldo += valor;
    }
    public double calculaRendimento(){
        return this.saldo * 0.1;
    }
    public String getDadosConta(){
        String dados = "Titular:  " + this.titular;
        dados += "\nNumero: " + this.numero;
        dados += "\nAgencia: " + this.agencia;
        dados += "\nSaldo: " + this.saldo;
        return dados;
    }
}
