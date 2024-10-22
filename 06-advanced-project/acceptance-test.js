import http from "k6/http";
import { sleep } from "k6";
export const options = {
  vus: 10,
  duration: "10s",
  thresholds: {
    http_req_duration: ["p(90)<10000"], // 90 percent of response times must be below 600ms
  },
};
export default function () {
  http.get(`http://${__ENV.SERVICE}`);
  sleep(1);
}
