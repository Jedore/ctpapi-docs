<p>请求查询组合合约安全系数</p>
<p>响应：OnRspQryCombInstrumentGuard</p>
<span class="anchor" id="cb67f7f9-83b3-443a-9de7-fbcfa3877d8f"></span>
## 1.函数原型
<p>virtual int ReqQryCombInstrumentGuard(CThostFtdcQryCombInstrumentGuardField *pQryCombInstrumentGuard, int nRequestID) = 0;</p>
<span class="anchor" id="b3abec60-456e-4be5-bd92-513a5bbd943b"></span>
## 2.参数
<p>pQryCombInstrumentGuard：组合合约安全系数查询</p>
<table><tr><th style="TEXT-ALIGN: center;">字段类型</th><th style="TEXT-ALIGN: center;">字段名称</th><th style="TEXT-ALIGN: center;">含义</th><th style="TEXT-ALIGN: center;">是否可作为过滤条件</th></tr><tr><td style="TEXT-ALIGN: left;">TThostFtdcBrokerIDType</td>
<td style="TEXT-ALIGN: left;">BrokerID</td>
<td style="TEXT-ALIGN: left;">经纪公司代码</td>
<td style="TEXT-ALIGN: left;">否</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcInstrumentIDType</td>
<td style="TEXT-ALIGN: left;">InstrumentID</td>
<td style="TEXT-ALIGN: left;">合约代码</td>
<td style="TEXT-ALIGN: left;">否</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcExchangeIDType</td>
<td style="TEXT-ALIGN: left;">ExchangeID</td>
<td style="TEXT-ALIGN: left;">交易所代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
</table>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="384c0ea9-74bf-46fd-bbcd-83c871b719e5"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="5b207aa1-9c5a-482c-8aa8-f39126f0b022"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="5fd1d1c6-9003-4e5a-b71f-e698dd5e1cdb"></span>
## 5.FAQ
<p>无</p>
