    // More API functions here:
// https://github.com/googlecreativelab/teachablemachine-community/tree/master/libraries/image

// the link to your model provided by Teachable Machine export panel
const URL = "https://teachablemachine.withgoogle.com/models/WXmTZBNlH/";

let model, webcam, labelContainer, maxPredictions;

// Load the image model and setup the webcam
async function init() {
        const modelURL = URL + "model.json";
const metadataURL = URL + "metadata.json";
// 2. start 버튼을 누를 시, 모델이 저장된 teachablemachine url에서
// 3. 모델 파일인 .json을 가져옴

// load the model and metadata
// Refer to tmImage.loadFromFiles() in the API to support files from a file picker
// or files from your local hard drive
// Note: the pose library adds "tmImage" object to your window (window.tmImage)
model = await tmImage.load(modelURL, metadataURL);
maxPredictions = model.getTotalClasses();
// 4. 가져온 모델 파일인 .json을 load 해줌

/*
// Convenience function to setup a webcam
const flip = true; // whether to flip the webcam
webcam = new tmImage.Webcam(200, 200, flip); // width, height, flip
await webcam.setup(); // request access to the webcam
await webcam.play();
window.requestAnimationFrame(loop);
*/
// 5. load가 된 후, 웹캠을 켜서 반복(loop)를 실행시킴 (loop로 이동)
// 13. 필요없는 웹캠 부분은 삭제

// append elements to the DOM
// document.getElementById("webcam-container").appendChild(webcam.canvas);
labelContainer = document.getElementById("label-container");
for (let i = 0; i < maxPredictions; i++) { // and class labels
    labelContainer.appendChild(document.createElement("div"));
        }
    }

/*
async function loop() {
    webcam.update(); // update the webcam frame
await predict();
window.requestAnimationFrame(loop);
    }
*/
// 6. 웹캠을 계속 업데이트하며 동물상에 맞는 이미지인지 예측을 반복해서 수행 (맨밑으로 이동)
// 11. 이미지는 한번의 업데이트로 예측을 하면 되기 때문에 반복문 삭제

// run the webcam image through the image model
async function predict() {
        // predict can take in an image, video or canvas html element
        /*
        const prediction = await model.predict(webcam.canvas);
        // 12. 웹캠 대신 업로드된 이미지를 넣어야 함
        */
        var image = document.getElementById("upload-image")
        // 18. 업로드될 이미지의 변수를 지정하고
        // 19. document.getElementById를 통해 문서에서 이미지에 해당하는 id를 가져오기
        const prediction = await model.predict(image, false);
        // 14. 이미지를 넣기 위해 구글링 (teachable machine GitHub)
        // 15. libraries -> image -> README를 통한 사용법 찾기
        // 16. Model - predict 부분에 이미지의 HTML 요소와 뒤집혔는지의 여부 입력을 확인
        /* 17.
            model.predict(
            image: HTMLImageElement | HTMLCanvasElement | HTMLVideoElement | ImageBitmap,
            flipped = false
            )
        */
       // 24. 업로드된 이미지를 가져오는 코드를 완성했다면,
       // 25. 앞서 정한 변수인 image를 webcam.canvas 대신 입력, 뒤집힘의 여부는 false
for (let i = 0; i < maxPredictions; i++) {
            const classPrediction =
prediction[i].className + ": " + prediction[i].probability.toFixed(2);
labelContainer.childNodes[i].innerHTML = classPrediction;
        }
    }
// 7. 예측 함수는 모델을 이용해서 웹캠의 이미지를 예측함
// 8. 그렇게 나온 예측 결과를 Teachable Machine 사이트에서 정한
// 9. class 이름 : 예측 정보 = HTML 요소에 넣어줌
// 10. 이미지 업로드를 통한 테스트기 때문에 웹캠 요소 삭제 (웹캠 들어간 것들 전부 삭제)

function readFile(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            var htmlPreview =
                '<img width="200" src="' + e.target.result + '" />' +
                '<p>' + input.files[0].name + '</p>';
            var wrapperZone = $(input).parent();
            var previewZone = $(input).parent().parent().find('.preview-zone');
            var boxZone = $(input).parent().parent().find('.preview-zone').find('.box').find('.box-body');

            wrapperZone.removeClass('dragover');
            previewZone.removeClass('hidden');
            boxZone.empty();
            boxZone.append(htmlPreview);
        };

        reader.readAsDataURL(input.files[0]);
    }
}

function reset(e) {
    e.wrap('<form>').closest('form').get(0).reset();
    e.unwrap();
}

$(".dropzone").change(function () {
    readFile(this);
});

$('.dropzone-wrapper').on('dragover', function (e) {
    e.preventDefault();
    e.stopPropagation();
    $(this).addClass('dragover');
});

$('.dropzone-wrapper').on('dragleave', function (e) {
    e.preventDefault();
    e.stopPropagation();
    $(this).removeClass('dragover');
});

$('.remove-preview').on('click', function () {
    var boxZone = $(this).parents('.preview-zone').find('.box-body');
    var previewZone = $(this).parents('.preview-zone');
    var dropzone = $(this).parents('.form-group').find('.dropzone');
    boxZone.empty();
    previewZone.addClass('hidden');
    reset(dropzone);
});

function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();
        reader.onload = function (e) {
            $('.image-upload-wrap').hide();
            $('.file-upload-image').attr('src', e.target.result);
            $('.file-upload-content').show();
            $('.image-title').html(input.files[0].name);
        };
        reader.readAsDataURL(input.files[0]);
    } else {
        removeUpload();
    }
}

function readURL(input) {
    if (input.files && input.files[0]) {

        var reader = new FileReader();

        reader.onload = function (e) {
            $('.image-upload-wrap').hide();

            $('.file-upload-image').attr('src', e.target.result);
            $('.file-upload-content').show();

            $('.image-title').html(input.files[0].name);
        };

        reader.readAsDataURL(input.files[0]);

    } else {
        removeUpload();
    }
}

function removeUpload() {
    $('.file-upload-input').replaceWith($('.file-upload-input').clone());
    $('.file-upload-content').hide();
    $('.image-upload-wrap').show();
}
$('.image-upload-wrap').bind('dragover', function () {
    $('.image-upload-wrap').addClass('image-dropping');
});
$('.image-upload-wrap').bind('dragleave', function () {
    $('.image-upload-wrap').removeClass('image-dropping');
});