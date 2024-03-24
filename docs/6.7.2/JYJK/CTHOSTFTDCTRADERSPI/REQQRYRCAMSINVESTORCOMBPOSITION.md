<p>请求RCAMS策略组合持仓查询，对应响应请求<a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYRCAMSINVESTORCOMBPOSITION/">OnRspQryRCAMSInvestorCombPosition</a></p>
<span class="anchor" id="0189f9cf-b3b9-4498-b187-c6c51064a3ce"></span>
## 1.函数原型
<p>virtual int ReqQryRCAMSInvestorCombPosition(CThostFtdcQryRCAMSInvestorCombPositionField *pQryRCAMSInvestorCombPosition, int nRequestID) = 0;</p>
<span class="anchor" id="38aedf5b-9ac1-4dda-a645-5502d9fd6fae"></span>
## 2.参数
<p>pQryRCAMSInvestorCombPosition：RCAMS策略组合持仓查询</p>
<table><tr><th style="TEXT-ALIGN: center;">字段类型</th><th style="TEXT-ALIGN: center;">字段名称</th><th style="TEXT-ALIGN: center;">含义</th><th style="TEXT-ALIGN: center;">是否可作为过滤条件</th></tr><tr><td style="TEXT-ALIGN: left;">TThostFtdcBrokerIDType</td>
<td style="TEXT-ALIGN: left;">BrokerID</td>
<td style="TEXT-ALIGN: left;">经纪公司代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcInvestorIDType</td>
<td style="TEXT-ALIGN: left;">InvestorID</td>
<td style="TEXT-ALIGN: left;">投资者代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcInstrumentIDType</td>
<td style="TEXT-ALIGN: left;">InstrumentID</td>
<td style="TEXT-ALIGN: left;">合约代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcInstrumentIDType</td>
<td style="TEXT-ALIGN: left;">CombInstrumentID</td>
<td style="TEXT-ALIGN: left;">组合合约代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
</table>
<span class="anchor" id="396110fb-bbf3-4698-9274-ce65498142aa"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="79265e82-a50d-4891-8ab8-afdbbe618821"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="13421ca2-1ce5-41ef-84b9-f4e348a938be"></span>
## 5.FAQ
<p>无</p>
