import http from "k6/http";
import { sleep } from "k6";
export const options = {
  vus: 10,
  duration: "20s",
  thresholds: {
    http_req_duration: ["p(90)<600"], // 95 percent of response times must be below 500ms
  },
};
export default function () {
  http.get("http://test.k6.io");
  sleep(1);
}
