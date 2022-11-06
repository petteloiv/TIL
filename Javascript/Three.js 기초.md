## 배경색 설정하기

```javascript
const renderer = new THREE.WebGL1Renderer({ canvas, antialias : true, alpha : true})
```



1. css로 설정
2. renderer에서 설정 
   - renderer.setClearColor()
   - 투명도 조절 : renderer.setClearAlpha(0~1사이의값)
3. scene에서 설정
   - 렌더러에서 설정한거 의미없어짐



## 빛 

```javascript
const light = new THREE.DirectionalLight(빛색상, 강도)
```

- 카메라랑 마찬가지로 position 줄 수 있다 
- scene.add(light) 해야지 씬에 등장 
- directional light은 태양광이랑 비슷한 빛



## 애니메이션 주기 

requestAnimationFrame()

리페인트 : 브라우저가 어떤 연산이 끝나서.. 위치 결정된 후에 픽셀 그리는 과정 

리페인트 진행되기 전에 콜백함수 호출 



#### 성능보정 

- 모든 컴퓨터에서 동일하게 보이게 

- 1. const clock = new THREE.clock()

     1. clock.getElapsedTime
     2. clock.getDelta 

  2. js 내장기능 사용

     - Date.now 

     - ```js
       let oldTime = Date.now 
       // 함수 안에서
       const newTime = Date.now 
       const deltaTime = newTime - oldTime 
       oldTime = newTime
       ```



## 안개 

안개는 scene에 추가



## 라이브러리를 이용한 애니메이션 

- 직접 동작 구현할 필요 없음 
- 좋음.. 
- Greensock / gsap



## Geometry / 모양 



#### 회전 

```js
import { OrbitControls } from "three/examples/jsm/controls/OrbitControls";

const controls = new OrbitControls(camera, renderer.domElement);
```

- 마우스로 돌려볼 수 있다



material 

```js
  const material = new THREE.MeshStandardMaterial({
    color: "hotpink",
    side: THREE.DoubleSide, //내부면도 보임 
    wireframe: true, //와이어프레임화
  });
```



## 카메라 컨트롤 



- three js 코어에는 포함되지 않기때문에 따로 import 해줘야한다



#### orbitcontrols

```js
import { OrbitControls } from "three/examples/jsm/controls/OrbitControls";

const controls = new OrbitControls(camera, renderer.domElement); 
// 인자 : 카메라, 캔버스 객체 가르키는 domelement
```

```js
aterial = new THREE.MeshStandardMaterial({
      color: `rgb(
			  ${50 + Math.floor(Math.random() * 205)},
				${50 + Math.floor(Math.random() * 205)},
				${50 + Math.floor(Math.random() * 205)}
				)
			`,
    });

// 안보이는거 방지하기 위해 기본으로 50 주고 랜덤값 최대치를 조정한다
```

```js
// 돌릴때 부드럽게 넘어간다

controls.enableDamping = true;

function draw () {
    controls.update();
}

// 기본 줌 설정 해제
controls.enableZoom = false;

// 멀어질 수 있는 거리 제한 (기본 무한정)
controls.maxDistance = 10;

// 가까워질 수 있는~ 
controls.minDistance = 10;

// 회전할 수 있는 각도 (min/ max)
controls.minPolarAngle = Math.PI / 4;
controls.minPolarAngle = THREE.MathUtils.degToRad(45);

// 회전 중심축 타겟으로 정하기 (x, y, z)
controls.target.set(2, 2, 2); 

// 자동 돌리기 & 속도 조절
controls.autoRotate = true;
controls.autoRotateSpeed = 50;
```



#### TrackballControls

- orbitcontrols과 다른점 
  - 수직으로도 회전이 다 된다 (orbit은 180도)



#### FlyControls

- draw 함수 안에서 update할 때 delta 값을 넣어줘야한다
- 조작 : wasd
  - r : 위 
  - f : 아래
- 마우스 올려두면 그 방향으로 천천 히  회전 (이동 XX).. 스피드 조절 가능

```js
controls.rollSpeed = 0.5;
controls.movementSpeed = 0.5;

// 마우스에 반응 X 드래그 필요
controls.dragToLook = true
```



#### FirstPersonControls 

- flycontrols의 대체 구현 (비슷함 ㅎㅎ)
  - 몇가지 기능 추가된 느낌..

```js
// 주변 둘러볼 수 없음! 움직일수만 있당 .. 
controls.activeLook = false
controls.lookSpeed = 0.5;
controls.autoFoward= true;
```



#### PointerLockControls

- update 메서드 없다! draw 안에 XXXXX
- user gesture 필요하당
  - event 따라서 control이 동작

```js
  controls.domElement.addEventListener("click", () => {
    controls.lock();
  });

// 시점에 수행해 줄 동작 있으면 수행해도 된다
  controls.addEventListener("lock", () => {
    console.log("lock!");
  });
  controls.addEventListener("unlock", () => {
    console.log("unlock!");
  });


```



#### DragControls

- 다른 애들과 매개변수에 들어가는 인자 다르당 

```js
// Controls 앞에 인자 들어감 내가 넣은건 배열 ,, 드래그 할 친구 넣으면 될둣
// mesh 선언 이전에 하면 오류 미친듯이 남
  const controls = new DragControls(meshes, camera, renderer.domElement);

// 어떤 것 드래그 했는지 알 수 있다 
  controls.addEventListener("dragstart", (e) => {
    console.log(e.object.name);
  });
```





###  PointerLockControls + 이동기능

---



#### keycontroller 작성 

```js
export class KeyController {
  constructor() {
    // 생성자
    this.keys = [];
      
    // 키 눌렀을 때 this.keys에 코드 들어가게하고 true 처리
    window.addEventListener("keydown", (e) => {
      this.keys[e.code] = true;
    });

    // 키 떼면 속성 삭제!
    window.addEventListener("keyup", (e) => {
      delete this.keys[e.code];
    });
  }
}

```



```js
import { KeyController } from "./KeyController";

  // 키보드 컨트롤
  const keyController = new KeyController();

function walk() {
    if (keyController.keys["KeyW"] || keyController.keys["ArrowUp"]) {
      controls.moveForward(0.02);
    }
    if (keyController.keys["KeyS"] || keyController.keys["ArrowDown"]) {
      controls.moveForward(-0.02);
    }
    if (keyController.keys["KeyD"] || keyController.keys["ArrowRight"]) {
      controls.moveRight(0.02);
    }
    if (keyController.keys["KeyA"] || keyController.keys["ArrowLeft"]) {
      controls.moveRight(-0.02);
    }
  }

function draw(){
    ...
    // 계속 실행시켜서 판별하는 용도로 사용
    walk()
}
```



## light (조명, 광원)



#### ambientlight 

- 은은하게 베이스로 깔아주는 조명
- 그림자 XX
- 이걸 기본으로 다른 조명 추가해주는 형태로 많이 쓴다

```js
  const light = new THREE.AmbientLight(색상, 강도(디폴트 1));
```

