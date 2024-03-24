<p>请求查询行情，只能查询当前快照，不能查询历史行情。</p>
<p>响应: <a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYDEPTHMARKETDATA/">OnRspQryDepthMarketData</a></p>
<span class="anchor" id="6e3b3ce9-cccf-4c54-b320-b4e405093e34"></span>
## 1.函数原型
<p>virtual int ReqQryDepthMarketData(CThostFtdcQryDepthMarketDataField *pQryDepthMarketData, int nRequestID) = 0;</p>
<span class="anchor" id="c9790d54-86ff-4136-b08f-2e14557b68bd"></span>
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
<span class="anchor" id="25060ecb-370e-401b-ac59-8f4d95000c03"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="1c0141e2-4c49-4996-be3f-18b4ee8e5106"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="52b65d5e-b328-4582-a15f-88f522689f1c"></span>
## 5.FAQ
<p>无</p>
