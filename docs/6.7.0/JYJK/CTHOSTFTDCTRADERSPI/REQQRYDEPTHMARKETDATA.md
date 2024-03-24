<p>请求查询行情，只能查询当前快照，不能查询历史行情。</p>
<p>响应: <a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYDEPTHMARKETDATA/">OnRspQryDepthMarketData</a></p>
<span class="anchor" id="31a8be7f-9cca-4e22-84b3-69a539b0e3b4"></span>
## 1.函数原型
<p>virtual int ReqQryDepthMarketData(CThostFtdcQryDepthMarketDataField *pQryDepthMarketData, int nRequestID) = 0;</p>
<span class="anchor" id="311bd82b-69a4-48b8-b487-0fde5bd719a7"></span>
## 2.参数
<p>pQryDepthMarketData：查询行情</p>
<table><tr><th style="TEXT-ALIGN: center;">字段类型</th><th style="TEXT-ALIGN: center;">字段名称</th><th style="TEXT-ALIGN: center;">含义</th><th style="TEXT-ALIGN: center;">是否可作为过滤条件</th></tr><tr><td style="TEXT-ALIGN: left;">TThostFtdcInstrumentIDType</td>
<td style="TEXT-ALIGN: left;">InstrumentID</td>
<td style="TEXT-ALIGN: left;">合约代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcExchangeIDType</td>
<td style="TEXT-ALIGN: left;">ExchangeID</td>
<td style="TEXT-ALIGN: left;">交易所代码</td>
<td style="TEXT-ALIGN: left;">否</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcOldInstrumentIDType</td>
<td style="TEXT-ALIGN: left;">reserve1</td>
<td style="TEXT-ALIGN: left;">保留的无效字段</td>
<td style="TEXT-ALIGN: left;">否</td>
</tr>
</table>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="0a46e09b-32c6-41c1-8edd-5417125a5392"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="20cbcf2b-ddb7-4718-9d50-31eb9699f09e"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="a9ea737f-f235-449e-9f2c-b2a26221d384"></span>
## 5.FAQ
<p>无</p>
