<p>用户发出获取短信验证码请求，暂不支持</p>
<p>响应: <a href="../../CTHOSTFTDCTRADERAPI/ONRSPGENUSERTEXT/">OnRspGenUserText</a></p>
<span class="anchor" id="85ab7ed6-00f9-4378-8070-a9fe966c8bba"></span>
## 1.函数原型
<p>virtual int ReqGenUserText(CThostFtdcReqGenUserTextField *pReqGenUserText, int nRequestID) = 0;</p>
<span class="anchor" id="f99f60dd-9bbe-4706-a445-533bdd6c5ff4"></span>
## 2.参数
<p>pReqGenUserText：用户发出获取安全安全登陆方法请求</p>
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
<span class="anchor" id="6a088ee8-d02b-4140-8f81-eeffd933be88"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="04c9fd2c-a8e2-457b-a580-54a5aeca9ea1"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="5df6f7b4-9657-44c5-8a32-434e0aa26f27"></span>
## 5.FAQ
<p>无</p>
