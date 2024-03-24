<p>用户发出获取图形验证码请求，暂不支持</p>
<p>响应: <a href="../../CTHOSTFTDCTRADERAPI/ONRSPGENUSERCAPTCHA/">OnRspGenUserCaptcha</a></p>
<span class="anchor" id="5ee6f592-2a6d-4c09-8e51-55d4147ffe98"></span>
## 1.函数原型
<p>virtual int ReqGenUserCaptcha(CThostFtdcReqGenUserCaptchaField *pReqGenUserCaptcha, int nRequestID) = 0;</p>
<span class="anchor" id="9d8fa9f3-e4c0-48c0-9a99-ef9fa2be3c3e"></span>
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
<span class="anchor" id="b0487808-5d48-464d-b519-52b1970a99bf"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="1ff71220-f155-4517-a670-77ec94cd0011"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="f9aa087f-4fc5-436b-88b7-c6cb5074a85a"></span>
## 5.FAQ
<p>无</p>
