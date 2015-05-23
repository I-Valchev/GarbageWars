# GarbageWars
Garbage Wars ELSYS competition 2015 (Second place achieved)

---
What was the task?
---

Describtion as officially provided by VMware: 

```
Once upon a time in the virtual world of Javatopia there was a Big-Cloud-City. The town lacked garbage collection and the memory of the city was constantly growing. 10 commercial waste collection companies were competing for the exclusive license to do the environmental services. The Big-Cloud-City consisted of 10 sectors and there were 10 garbage cars in it, every company had one car in each sector. The rules for garbage collections in the virtual world of Javatopia were unexpectedly similar to the rules for garbage collection in the Java Language we all know. Each sector contains some regular objects and some system object. System object cannot be collected. Every regular object can be collected only if there is no way to reach it by following the references from the system objects. 

As this is a war, your program has to collect more objects than other programs running at the same time. Beware, if you don't collect the objects correctly, you car will explode. While repairing it, you will lose valuable time. Meanwhile your competitors can collect all the garbage.
```

---
How the task was solved?
---

The task was solved by separating the big problem into small relatively easily-solved challenges. Having created the data structure to contain edges, the team created an algorithm to fill the structure with real data (removing roots and their children). Then we used аebt-first search (DFS) algorithm, improving it to find the most suitable solution for the given task (we aim to collect the longest trajectory)

---
The result
---

The team scored second, collecting about 30% of all edges (which was a good result bearing in mind the fact that there were about 15 teams competing). Having accoplished such result, the two member team was awared by the VMware employees who conducted the competition.f