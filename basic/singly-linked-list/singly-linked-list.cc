#include <iostream>

// Definition for singly-linked list.
struct SinglyListNode {
    int val;
    SinglyListNode* next;
    SinglyListNode(int x) : val(x), next(nullptr) {}
};

class MyLinkedList {
  SinglyListNode* head;
  SinglyListNode* tail;
  int size = 0;
 public:
  /** Initialize your data structure here. */
  MyLinkedList() {
    head = nullptr;
    tail = nullptr;
    size = 0;
  }
  ~MyLinkedList() {
    SinglyListNode* traverse = head;
    while (traverse) {
      auto next_node = traverse->next;
      delete traverse;
      traverse = next_node;
    }
  }

  /** Get the value of the index-th node in the linked list. If the index is invalid, return -1. */
  int get(int index) {
    if (index < 0 || index >= size) {
      return -1;
    }
    return getNode(index)->val;
  }

  /** Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list. */
  void addAtHead(int val) {
    SinglyListNode* node = new SinglyListNode(val);
    node->next = this->head;
    this->head = node;
    if (this->tail == nullptr) {
      this->tail = node;
    }
    ++size;
  }

  /** Append a node of value val to the last element of the linked list. */
  void addAtTail(int val) {
    SinglyListNode* node = new SinglyListNode(val);
    if (this->tail) {
      this->tail->next = node;
      this->tail = node;
    } else {
      this->tail = node;
      this->head = node;
    }
    ++size;
  }

  /** Add a node of value val before the index-th node in the linked list.
   * If index equals to the length of linked list,
   * the node will be appended to the end of linked list.
   * If index is greater than the length, the node will not be inserted. */
  void addAtIndex(int index, int val) {
    // Case 3
    if (index > size || index < 0) return;
    if (index == 0) {
      this->addAtHead(val);
      return;
    };
    if (index == size) {
      this->addAtTail(val);
      return;
    }
    // insert a node
    SinglyListNode* node = new SinglyListNode(val);
    SinglyListNode* traverse = getNode(index-1);
    // Fix the new node next pointer
    node->next = traverse->next;
    traverse->next = node;
    ++size;
  }

  /** Delete the index-th node in the linked list, if the index is valid. */
  void deleteAtIndex(int index) {
    if (index >= size || index < 0) return;

    SinglyListNode* to_be_delete;
    // handle head
    if (index == 0) {
      // remove head
      to_be_delete = head;
      head = head->next;
      delete to_be_delete;
      --size;
      return;
    }
    // handle tail
    if (index == size-1) {
      // remove head
      to_be_delete = tail;
      auto prev_node = getNode(size-2);
      tail = prev_node;
      tail->next = nullptr;
      delete to_be_delete;
      --size;
      return;
    }

    SinglyListNode* prev_node = getNode(index-1);
    to_be_delete = prev_node->next;
    prev_node->next = to_be_delete->next;
    delete to_be_delete;
    --size;
  }

  void show() {
    SinglyListNode* traverse;
    traverse = head;
    if (traverse == nullptr) {
      return;
    }
    while (traverse) {
      std::cout << traverse->val;
      std::cout << "->";
      traverse = traverse->next;
    }
    std::cout << "x" << std::endl;
  }
 private:
  SinglyListNode* getNode(int index) {
    if (index == 0) return head;
    if (index == size-1) return tail;
    SinglyListNode* traverse = head;
    for (int i=0; i < index; ++i) {
      traverse = traverse->next;
    }
    return traverse;
  }
};

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList* obj = new MyLinkedList();
 * int param_1 = obj->get(index);
 * obj->addAtHead(val);
 * obj->addAtTail(val);
 * obj->addAtIndex(index,val);
 * obj->deleteAtIndex(index);
 */

int main() {
  MyLinkedList linked_list = MyLinkedList();
  // linked_list.addAtHead(7);
  // linked_list.addAtHead(2);
  // linked_list.addAtHead(1);
  // linked_list.addAtIndex(3, 0);
  // linked_list.deleteAtIndex(2);
  // linked_list.addAtHead(6);
  // linked_list.addAtTail(4);
  // std::cout << linked_list.get(4) << std::endl;
  // linked_list.addAtHead(4);
  // linked_list.addAtIndex(5, 0);
  // linked_list.addAtHead(6);
  // linked_list.addAtIndex(1, 100);
  // linked_list.addAtIndex(1, 200);
  // std::cout << linked_list.get(0) << std::endl;
  // std::cout << linked_list.get(1) << std::endl;
  // linked_list.show();
  linked_list.addAtHead(1);
  linked_list.addAtTail(3);
  linked_list.addAtIndex(1, 2);
  linked_list.show();
  // std::cout << linked_list.get(1) << std::endl;
  // std::cout << linked_list.get(2) << std::endl;
  linked_list.deleteAtIndex(1);
  linked_list.show();
  std::cout << linked_list.get(1) << std::endl;
}
