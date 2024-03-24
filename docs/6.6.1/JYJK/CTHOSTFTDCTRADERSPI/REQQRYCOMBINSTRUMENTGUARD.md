<p>请求查询组合合约安全系数</p>
<p>响应：<a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYCOMBINSTRUMENTGUARD/">OnRspQryCombInstrumentGuard</a></p>
<span class="anchor" id="e49e92d3-233d-4411-816f-de3265946cf0"></span>
## 1.函数原型
<p>virtual int ReqQryCombInstrumentGuard(CThostFtdcQryCombInstrumentGuardField *pQryCombInstrumentGuard, int nRequestID) = 0;</p>
<span class="anchor" id="2be7900e-0f07-4ff5-943b-3fa1734a9d56"></span>
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
<span class="anchor" id="c56027e9-f0ad-4dc2-a6d4-24946ef70f7a"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="aae99aa1-747d-4d2b-a678-7b3f81c9efd0"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="914606ba-b89b-4fc5-8409-a43293a156bf"></span>
## 5.FAQ
<p>无</p>
