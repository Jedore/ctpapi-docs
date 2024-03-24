<p>用户发出获取短信验证码请求，暂不支持</p>
<p>响应: <a href="../../CTHOSTFTDCTRADERAPI/ONRSPGENUSERTEXT/">OnRspGenUserText</a></p>
<span class="anchor" id="acc62620-fa82-445f-99d0-7ce062211a59"></span>
## 1.函数原型
<p>virtual int ReqGenUserText(CThostFtdcReqGenUserTextField *pReqGenUserText, int nRequestID) = 0;</p>
<span class="anchor" id="d737bae3-631b-466e-99e7-0353e8924282"></span>
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
<span class="anchor" id="3c7d178e-1194-4d01-893b-bbb171588b6e"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="ab3dc839-b544-4b1f-829f-653d41e2aba5"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="ca11e12b-ea50-42c3-910a-59298580588e"></span>
## 5.FAQ
<p>无</p>
