<p>用户发出获取图形验证码请求，暂不支持</p>
<p>响应: OnRspGenUserCaptcha</p>
<span class="anchor" id="6adb0f14-0611-449e-9c72-7d933e0d5f75"></span>
## 1.函数原型
<p>virtual int ReqGenUserCaptcha(CThostFtdcReqGenUserCaptchaField *pReqGenUserCaptcha, int nRequestID) = 0;</p>
<span class="anchor" id="3ffd70cd-8f1c-4cf4-bc74-6eeca18ea6be"></span>
## 2.参数
<p>pReqGenUserCaptcha：用户发出获取安全安全登陆方法请求</p>
<table><tr><th style="TEXT-ALIGN: center;">字段类型</th><th style="TEXT-ALIGN: center;">字段名称</th><th style="TEXT-ALIGN: center;">含义</th><th style="TEXT-ALIGN: center;">值</th></tr><tr><td style="TEXT-ALIGN: left;">TThostFtdcDateType</td>
<td style="TEXT-ALIGN: left;">TradingDay</td>
<td style="TEXT-ALIGN: left;">交易日</td>
<td style="TEXT-ALIGN: left;">无</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcBrokerIDType</td>
<td style="TEXT-ALIGN: left;">BrokerID</td>
<td style="TEXT-ALIGN: left;">经纪公司代码</td>
<td style="TEXT-ALIGN: left;">无</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcUserIDType</td>
<td style="TEXT-ALIGN: left;">UserID</td>
<td style="TEXT-ALIGN: left;">用户代码</td>
<td style="TEXT-ALIGN: left;">无</td>
</tr>
</table>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="868b38d5-dc93-4079-a1f6-cb8780984b3e"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="5d0fce78-70c1-4366-b039-40491f9b97e4"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="e9c9482d-2d81-4bd0-8d9e-6ad28a3be3dd"></span>
## 5.FAQ
<p>无</p>
