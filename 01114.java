class Foo {
    boolean executedFirst;
    boolean executedSecond;
    boolean executedThird;

    Object lock = new Object();

    public Foo() {
        executedFirst = false;
        executedSecond = false;
    }

    public void first(Runnable printFirst) throws InterruptedException {
        
        // printFirst.run() outputs "first". Do not change or remove this line.
        synchronized(lock){
            printFirst.run();
            executedFirst = true;
        }
    }

    public void second(Runnable printSecond) throws InterruptedException {
        
        // printSecond.run() outputs "second". Do not change or remove this line.
        while(executedFirst == false){
            Thread.yield();
        }

        synchronized(lock){
            printSecond.run();
            executedSecond = true;
        }
    }

    public void third(Runnable printThird) throws InterruptedException {
        
        // printThird.run() outputs "third". Do not change or remove this line.

        while(executedSecond == false){
            Thread.yield();
        }
        printThird.run();
    }
}