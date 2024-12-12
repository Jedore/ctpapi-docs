<p>请求查询行情，只能查询当前快照，不能查询历史行情。</p>
<p>响应: <a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYDEPTHMARKETDATA/">OnRspQryDepthMarketData</a></p>
<span class="anchor" id="91b4167c-c4a8-47bc-b729-bd34fa36a69a"></span>
## 1.函数原型
<p>virtual int ReqQryDepthMarketData(CThostFtdcQryDepthMarketDataField *pQryDepthMarketData, int nRequestID) = 0;</p>
<span class="anchor" id="ce588375-ebae-4f5b-910f-b2d93f793458"></span>
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
<tr><td style="TEXT-ALIGN: left;">TThostFtdcProductClassType</td>
<td style="TEXT-ALIGN: left;">ProductClass</td>
<td style="TEXT-ALIGN: left;">产品类型</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
</table>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="4e5f1c2d-e4d3-4256-900a-ac2942a7e325"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="a1ac00a5-e269-4791-88ed-d407b2c17ae5"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="ae2192e0-138c-4e00-9bd4-5dc559ce2b74"></span>
## 5.FAQ
<p>无</p>
