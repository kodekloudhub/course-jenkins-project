import http from "k6/http";
import { sleep } from "k6";
export const options = {
  vus: 10,
  duration: "10s",
  thresholds: {
    http_req_duration: ["p(90)<600"], // 95 percent of response times must be below 500ms
  },
};
export default function () {
  http.get(`http://${__ENV.SERVICE}`);
  sleep(1);
}
