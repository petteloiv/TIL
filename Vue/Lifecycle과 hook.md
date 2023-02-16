## lifecycle
> Vue 인스턴스나 컴포넌트가 생성될 때 거치게 되는 과정 
> 인스턴스가 생성된 후 우리 눈에 보여지고, 사라지기까지의 단계 

![](vue의lifecycle과hook.assets/image.png)


**1. 생성 create **
- 데이터만 존재하는 단계

**2. DOM에 부착 mount **
- `<template>` 사이에 있던 것을 HTML로 바꿔주고 컴포넌트 생성 단계에서 index.html에 부착한다

**3. 업데이트 update **
- 데이터가 변하면 컴포넌트가 재렌더링! 
  

**4. 없어진다! destroy**
- 컴포넌트 삭제~

## Lifecycle Hook 
> 라이프사이클 단계마다 실행될 수 있는 함수와 같은 라이프사이클 훅
> Hook을 걸어서 라이프사이클 중간에 원하는 코드를 실행 가능하다 

- `<script>` 부분에 작성하면 된다 
- `beforeCreate`, `created`, `beforeMount`, `mounted`, `beforeUpdate`(), `updated`, `beforeUnmount`, `unmounted`
---

### 1. Create
- 컴포넌트 초기화 단계 
- 라이프사이클에서 가장 먼저 실행! 
- DOM 추가 되기 전 / 서버 렌더링 중에도 실행 

-> **클라이언트&서버 렌더링 과정 모두에서 컴포넌트 설정할 필요 있다면 여기서 처리**

#### beforeCreate

```js
export default{
    data() {
        return {
            msg: 'hello';
        }
    },
    beforeCreate(){
        console.log(this.msg); // undefined! 접근 불가
    }
}

```
- 가장 먼저 실행
- Vue 인스턴스 초기화 된 직후에 발생! 
- 컴포넌트가 DOM에 추가되기 전이라 data, method 등에도 접근 불가

#### created

- 템플릿 및 가상 DOM 부착 전에 실행!
- data, event 활성화되어 접근 가능 

- 데이터 초기화시에 사용
- 부모 > 자식 순으로 created 훅 실행 

---

### 2. Mount 
- DOM 부착 단계
- 가장 많이 사용! 초기 렌더링 전후에 바로 컴포넌트에 접근 가능
- 서버 렌더링 실행되는 동안에는 실행되지 않는다 

-> **초기 렌더링 직전. 직후에 DOM 접근하거나 수정할 때 사용 **

#### beforeMount 

```js
export default{
  beforeMount(){
        console.log('beforeMount'); // undefined! 접근 불가
    }
}
```
- DOM에 부착하기 직전에 호출!
- 템플릿 유무 확인한 후 템플릿 렌더링 한 상태
- 가상 DOM 생성된 상태지만 실제 DOM에 부착되지 않은 상태

---

### 3. Update 
- 컴포넌트에서 쓰는 반응형 속성들이 변경되거나 리렌더링 될 때 호출! 

-> **컴포넌트가 다시 렌더링되는 시기를 알아야 하는 경우에 사용 **

#### beforeUpdate 
```js
export default {
  data() {
    return {
      counter: 0
    }
  },

  created() {
    setInterval(() => {
      this.counter++
    }, 1000)
  },

  beforeUpdate() {
    console.log(`At this point, Virtual DOM has not re-rendered or patched yet.`)
    // Logs the counter value every second, before the DOM updates.
    console.log(this.counter)
  }
}
```

- 컴포넌트 데이터 변경되고 DOM 다시 렌더링 되기 전에 실행
- 렌더링 되기 전에 데이터 신규 상태 가져와야하는 경우에 사용

#### updated
- 컴포넌트 데이터가 변경되어 DOM이 리렌더링 된 후 실행!

---

### Destroy
- 컴포넌트 해체되고 DOM에서 제거될 때 실행된다! 

#### beforeDestroy 
- 해체 직전에 실행 
- 컴포넌트는 여전히 존재하고 작동한다
- 이벤트 리스너 등 정리하는데에 사용 

```js
export default {
  beforeDestroy() {
    console.log('beforeDestory');
  }
}
```

#### destroyed
- 컴포넌트 해체된 후 호출 
- 컴포넌트 파괴된 것을 원격 서버에 알려야 하는 경우 사용!

>** Reference** ✍
>https://vuejs.org/guide/essentials/lifecycle.html