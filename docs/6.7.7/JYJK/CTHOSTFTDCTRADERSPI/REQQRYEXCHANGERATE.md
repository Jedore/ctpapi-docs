<p>请求查询汇率</p>
<p>响应：<a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYEXCHANGERATE/">OnRspQryExchangeRate</a></p>
<span class="anchor" id="68068672-054b-41a6-b93c-9c382cd5e815"></span>
## 1.函数原型
<p>virtual int ReqQryExchangeRate(CThostFtdcQryExchangeRateField *pQryExchangeRate, int nRequestID) = 0;</p>
<span class="anchor" id="5a3e42ef-1cc0-4203-9266-3248e2139283"></span>
## 2.参数
<p>pQryExchangeRate：查询汇率</p>
<table><tr><th style="TEXT-ALIGN: center;">字段类型</th><th style="TEXT-ALIGN: center;">字段名称</th><th style="TEXT-ALIGN: center;">含义</th><th style="TEXT-ALIGN: center;">是否可作为过滤条件</th></tr><tr><td style="TEXT-ALIGN: left;">TThostFtdcBrokerIDType</td>
<td style="TEXT-ALIGN: left;">BrokerID</td>
<td style="TEXT-ALIGN: left;">经纪公司代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcCurrencyIDType</td>
<td style="TEXT-ALIGN: left;">FromCurrencyID</td>
<td style="TEXT-ALIGN: left;">源币种</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcCurrencyIDType</td>
<td style="TEXT-ALIGN: left;">ToCurrencyID</td>
<td style="TEXT-ALIGN: left;">目标币种</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
</table>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="cd6f07de-3b27-4d29-b5ab-6729f12bae80"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="14cc333d-ddbc-4bf9-9ea7-4847612798f9"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="1f4219e4-b74d-41ba-b2f9-f9cf8fc067bc"></span>
## 5.FAQ
<p>无</p>
