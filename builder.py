public class Pizza {
 
    private float totalPrice = 0;
 
    private Size;
    private Crust;
    private Cheese;
    private Topping;
     
    public Size getSize() {
        return size;
    }
 
    public void setSize(Size) {
        this.size = size;
    }
 
    public Crust getCrust() {
        return crust;
    }
 
    public void setCrust(Crust) {
        this.crust = crust;
    }
 
    public Cheese getCheese() {
        return cheese;
    }
 
    public void setCheese(Cheese) {
        this.cheese = cheese;
    }
 
    public Topping getTopping() {
        return topping;
    }
 
    public void setTopping(Topping) {
        this.topping = topping;
    }
 
    
    public float getTotalPrice() {
        return totalPrice;
    }
 
    public void addToPrice(float price) {
        this.totalPrice = totalPrice + price;
    }
}
