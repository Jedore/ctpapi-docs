<p>请求查询分类合约，对应响应请求<a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYCLASSIFIEDINSTRUMENT/">OnRspQryClassifiedInstrument</a></p>
<p>详见  <a href="../../../6.5.1BBGXSMBCSM/">6.5.1版本更新说明补充说明</a></p>
<span class="anchor" id="c1550bf0-0b37-45db-9c2e-5553448b9117"></span>
## 1.函数原型
<p>virtual int ReqQryClassifiedInstrument(CThostFtdcQryClassifiedInstrumentField *pQryClassifiedInstrument, int nRequestID) = 0;</p>
<span class="anchor" id="eb469d6e-97ba-4b3a-9b26-4c4b32aef9c0"></span>
## 2.参数
<p>pQryClassifiedInstrument：查询分类合约</p>
<table><tr><th style="TEXT-ALIGN: center;">字段类型</th><th style="TEXT-ALIGN: center;">字段名称</th><th style="TEXT-ALIGN: center;">含义</th><th style="TEXT-ALIGN: center;">是否可作为过滤条件</th></tr><tr><td style="TEXT-ALIGN: left;">TThostFtdcInstrumentIDType</td>
<td style="TEXT-ALIGN: left;">InstrumentID</td>
<td style="TEXT-ALIGN: left;">合约代码</td>
<td style="TEXT-ALIGN: left;">否</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcExchangeIDType</td>
<td style="TEXT-ALIGN: left;">ExchangeID</td>
<td style="TEXT-ALIGN: left;">交易所代码</td>
<td style="TEXT-ALIGN: left;">否</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcExchangeInstIDType</td>
<td style="TEXT-ALIGN: left;">ExchangeInstID</td>
<td style="TEXT-ALIGN: left;">合约在交易所的代码</td>
<td style="TEXT-ALIGN: left;">否</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcInstrumentIDType</td>
<td style="TEXT-ALIGN: left;">ProductID</td>
<td style="TEXT-ALIGN: left;">产品代码</td>
<td style="TEXT-ALIGN: left;">否</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcTradingTypeType</td>
<td style="TEXT-ALIGN: left;">TradingType</td>
<td style="TEXT-ALIGN: left;">合约交易状态</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcClassTypeType</td>
<td style="TEXT-ALIGN: left;">ClassType</td>
<td style="TEXT-ALIGN: left;">合约分类类型</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
</table>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="48875b1d-39d1-4be8-bbac-9be5d0269842"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="1b839c85-02c3-4ead-98d3-e0ed9b87e811"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="8aa810fd-a1a0-4cdf-a829-47beb4b79464"></span>
## 5.FAQ
<p>无</p>
