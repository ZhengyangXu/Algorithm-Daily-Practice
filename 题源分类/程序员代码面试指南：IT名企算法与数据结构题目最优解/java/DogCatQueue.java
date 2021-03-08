import java.util.LinkedList;
import java.util.Queue;

import javax.management.RuntimeErrorException;

// 猫狗队列【题目】宠物、狗和猫的类如下：[插图]实现一种狗猫队列的结构，
// 要求如下：
// ● 用户可以调用add方法将cat类或dog类的实例放入队列中；
// ● 用户可以调用pollAll方法，将队列中所有的实例按照进队列的先后顺序依次弹出；
// ● 用户可以调用pollDog方法，将队列中dog类的实例按照进队列的先后顺序依次弹出；
// ● 用户可以调用pollCat方法，将队列中cat类的实例按照进队列的先后顺序依次弹出；● 用户可以调用isEmpty方法，检查队列中是否还有dog或cat的实例；● 用户可以调用isDogEmpty方法，
// 检查队列中是否有dog类的实例；
// ● 用户可以调用isCatEmpty方法，检查队列中是否有cat类的实例。

public class DogCatQueue {

    private Queue<PetEnterQueue> dogQ;
    private Queue<PetEnterQueue> catQ;
    private long count;

    public DogCatQueue() {
        this.dogQ = new LinkedList<PetEnterQueue>();
        this.catQ = new LinkedList<PetEnterQueue>();
        this.count = 0;
    }

    public void add(Pet pet) {
        if (pet.getPetType().equals("dog")) {
            this.dogQ.add(new PetEnterQueue(pet, this.count++));

        } else if (pet.getPetType().equals("cat")) {
            this.catQ.add(new PetEnterQueue(pet, this.count++));
        } else {
            throw new RuntimeException("err,not dog or cat");
        }
    }

    public String pollAll() {
        if (!this.dogQ.isEmpty() && !this.catQ.isEmpty()) {
            if (this.dogQ.peek().getCount() < this.catQ.peek().getCount()) {
                return this.dogQ.poll().getPetName();
            } else {
                return this.catQ.poll().getPetName();
            }
        } else if (!this.dogQ.isEmpty()) {
            return this.dogQ.poll().getPetName();
        } else if (!this.catQ.isEmpty()) {
            return this.catQ.poll().getPetName();
        } else {
            throw new RuntimeException("err,queue is empty");
        }
    }

    public Dog pollDog() {
        if (!this.isDogQueueEmpty()) {
            return (Dog) this.dogQ.poll().getPet();
        } else {
            throw new RuntimeException("dog queue is empty");
        }
    }

    public Cat pollCat() {
        if (!this.isCatQueueEmpty()) {
            return (Cat) this.catQ.poll().getPet();
        } else {
            throw new RuntimeException("Cat queue is empty");
        }
    }

    public boolean isEmpty() {
        return this.dogQ.isEmpty() && this.catQ.isEmpty();
    }

    public boolean isDogQueueEmpty() {
        return this.dogQ.isEmpty();
    }

    public boolean isCatQueueEmpty() {
        return this.catQ.isEmpty();
    }

    public static void main(String args[]) {
        Dog dog1 = new Dog("dog1");
        Dog dog2 = new Dog("dog2");
        Dog dog3 = new Dog("dog3");
        Dog dog4 = new Dog("dog4");
        Dog dog5 = new Dog("dog5");
        Cat cat1 = new Cat("cat1");
        Cat cat2 = new Cat("cat2");
        Cat cat3 = new Cat("cat3");
        Cat cat4 = new Cat("cat4");
        Cat cat5 = new Cat("cat5");

        DogCatQueue dogcatqueue1 = new DogCatQueue();
        dogcatqueue1.add(dog1);
        dogcatqueue1.add(dog2);
        dogcatqueue1.add(dog3);
        dogcatqueue1.add(cat1);
        dogcatqueue1.add(dog4);
        dogcatqueue1.add(cat2);
        dogcatqueue1.add(cat3);

        System.out.println(dogcatqueue1.pollAll());

    }

}

class Pet {
    private String type;

    public Pet(String type) {
        this.type = type;
    }

    public String getPetType() {
        return this.type;
    }

}

class Dog extends Pet {
    private String name;

    public Dog() {
        super("dog");
    }

    public Dog(String name) {
        this();
        this.name = name;

    }

    public String getName(){
        return name;
    }
}

class Cat extends Pet {
    private String name;

    public Cat() {
        super("cat");
    }

    public Cat(String name) {
        this();
        this.name = name;
    }

    public String getName(){
        return name;
    }
}

class PetEnterQueue {
    private Pet pet;
    private long count;

    public PetEnterQueue(Pet pet, long count) {
        this.pet = pet;
        this.count = count;
    }

    public Pet getPet() {
        return this.pet;
    }

    public String getName() {
        return this.pet.
    }


    public long getCount() {
        return this.count;
    }

    public String getEnterPetType() {
        return this.pet.getPetType();
    }
}