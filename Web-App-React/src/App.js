import "./App.css";
import { Camera } from "@mediapipe/camera_utils";
import { useEffect, useRef } from "react";
import { Hands } from "@mediapipe/hands";
import { processLandmark } from "./handKeyPointsClassifier";

const maxVideoWidth = 960;
const maxVideoHeight = 540;
const detectionInterval = 2.5 * 1000;
const labels = ["Open", "Close", "Peace", "Thumbsup", "Ok"];
const labelsToDraw = ["Peace", "Thumbsup", "Ok"];

function App() {
  const camera = useRef(null);
  const hands = useRef(null);
  const videoElement = useRef(null);
  const canvasEl = useRef(null);
  let startTime = new Date().getTime();
  let labelToDraw = "";

  useEffect(() => {
    camera.current = new Camera(videoElement.current, {
      facingMode: "user",
      onFrame: async () => {
        await hands.current.send({ image: videoElement.current });
      },
      width: maxVideoWidth,
      height: maxVideoHeight,
    });
    camera.current.start();
  }, []);

  useEffect(() => {
    if (!hands || !hands.current) {
      loadHands();
    }
  }, [hands]);

  const loadHands = () => {
    try {
      hands.current = new Hands({
        locateFile: (file) => {
          return `https://cdn.jsdelivr.net/npm/@mediapipe/hands/${file}`;
        },
      });
      hands.current.setOptions({
        maxNumHands: 1,
        modelComplexity: 1,
        minDetectionConfidence: 0.9,
        minTrackingConfidence: 0.8,
      });
      hands.current.onResults(onResults);
    } catch (e) {
      console.log(e);
    }
  };

  async function onResults(results) {
    if (canvasEl.current) {
      const ctx = canvasEl.current.getContext("2d");
      ctx.save();
      ctx.clearRect(0, 0, canvasEl.current.width, canvasEl.current.height);
      ctx.drawImage(results.image, 0, 0, maxVideoWidth, maxVideoHeight);
      if (!results) return;
      if (startTime + detectionInterval < new Date().getTime()) {
        labelToDraw = "";
      }
      labelToDraw && draw(ctx, labelToDraw);
      if (results.multiHandLandmarks) {
        for (const [index, landmarks] of results.multiHandLandmarks.entries()) {
          processLandmark(landmarks, results.image)
            .then((r) => {
              const l = labels[r];
              if (startTime + detectionInterval < new Date().getTime()) {
                if (labelsToDraw.includes(l)) {
                  labelToDraw = l;
                  startTime = new Date().getTime();
                  console.log(labelToDraw);
                }
              }
            })
            .catch((e) => {
              console.log(e);
            });
        }
      }
      ctx.restore();
    }
  }

  const draw = (ctx, label) => {
    const img = new Image();
    img.onload = () => {
      ctx.drawImage(img, 20, 20, 200, 100);
    };
    switch (label) {
      case "Peace":
        img.src = "/images/peace.png";
        break;
      case "Thumbsup":
        img.src = "/images/thumbs_up.png";
        break;
      case "Ok":
        img.src = "/images/ok.png";
        break;
    }
  };

  return (
    <div className="App">
      <div
        style={{
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
          flexDirection: "column",
        }}
      >
      <h1>Dynamic Vision</h1>
        <video
          style={{ display: "none" }}
          className="video"
          playsInline
          ref={videoElement}
        />
        <canvas ref={canvasEl} width={maxVideoWidth} height={maxVideoHeight} />
      </div>
    </div>
  );
}

export default App;
