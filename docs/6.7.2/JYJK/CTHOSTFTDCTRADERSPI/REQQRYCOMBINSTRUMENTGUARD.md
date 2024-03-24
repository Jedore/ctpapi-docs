<p>请求查询组合合约安全系数</p>
<p>响应：<a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYCOMBINSTRUMENTGUARD/">OnRspQryCombInstrumentGuard</a></p>
<span class="anchor" id="f895efa2-686a-4b03-a8d6-4509e325f7ff"></span>
## 1.函数原型
<p>virtual int ReqQryCombInstrumentGuard(CThostFtdcQryCombInstrumentGuardField *pQryCombInstrumentGuard, int nRequestID) = 0;</p>
<span class="anchor" id="df7fa662-4cb4-4ee5-bc81-9230008d1d9c"></span>
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
<span class="anchor" id="9e7531b6-40b6-420a-a722-6e4c8a7b3772"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="856b819f-a094-4e0c-be34-5d34cc179c53"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="bb93162e-7125-46d0-9bfc-375816398158"></span>
## 5.FAQ
<p>无</p>
