<p>请求查询行情，只能查询当前快照，不能查询历史行情。</p>
<p>响应: <a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYDEPTHMARKETDATA/">OnRspQryDepthMarketData</a></p>
<span class="anchor" id="f6fe1a9b-0486-481c-80b9-1626cefab682"></span>
## 1.函数原型
<p>virtual int ReqQryDepthMarketData(CThostFtdcQryDepthMarketDataField *pQryDepthMarketData, int nRequestID) = 0;</p>
<span class="anchor" id="5ea3d619-95bb-4743-8821-3e27faadd335"></span>
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
<span class="anchor" id="46b74fbf-e382-462d-a262-e8440d3c161a"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="623b69ff-0424-4f3e-8ac0-e0e80274ed0a"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="4c31e4ac-f248-4bc6-9743-9fd8c6391d43"></span>
## 5.FAQ
<p>无</p>
