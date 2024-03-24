<p>请求查询经纪公司交易算法</p>
<p>响应: <a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYBROKERTRADINGALGOS/">OnRspQryBrokerTradingAlgos</a></p>
<span class="anchor" id="d1b706b7-674b-4c2c-857d-38e7e13e8cd9"></span>
## 1.函数原型
<p>virtual int ReqQryBrokerTradingAlgos(CThostFtdcQryBrokerTradingAlgosField *pQryBrokerTradingAlgos, int nRequestID) = 0;</p>
<span class="anchor" id="21dc95ff-2335-4ed6-92b1-2efd604938d5"></span>
## 2.参数
<p>pQryBrokerTradingAlgos：查询经纪公司交易算法</p>
<table><tr><th style="TEXT-ALIGN: center;">字段类型</th><th style="TEXT-ALIGN: center;">字段名称</th><th style="TEXT-ALIGN: center;">含义</th><th style="TEXT-ALIGN: center;">是否可作为过滤条件</th></tr><tr><td style="TEXT-ALIGN: left;">TThostFtdcBrokerIDType</td>
<td style="TEXT-ALIGN: left;">BrokerID</td>
<td style="TEXT-ALIGN: left;">经纪公司代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcExchangeIDType</td>
<td style="TEXT-ALIGN: left;">ExchangeID</td>
<td style="TEXT-ALIGN: left;">交易所代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcInstrumentIDType</td>
<td style="TEXT-ALIGN: left;">InstrumentID</td>
<td style="TEXT-ALIGN: left;">合约代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcOldInstrumentIDType</td>
<td style="TEXT-ALIGN: left;">reserve1</td>
<td style="TEXT-ALIGN: left;">保留的无效字段</td>
<td style="TEXT-ALIGN: left;">否</td>
</tr>
</table>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="1fd106ce-f5cb-4649-aeac-df89e958fad3"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="6a35e098-ac46-4a38-8673-ecf57c640422"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="ef03babb-136c-4f7a-8106-7a7abf1d3f70"></span>
## 5.FAQ
<p>无</p>
