<p>请求RCAMS策略组合持仓查询，对应响应请求<a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYRCAMSINVESTORCOMBPOSITION/">OnRspQryRCAMSInvestorCombPosition</a></p>
<span class="anchor" id="b1a3ee0f-422c-4058-a5ff-8449e46c8335"></span>
## 1.函数原型
<p>virtual int ReqQryRCAMSInvestorCombPosition(CThostFtdcQryRCAMSInvestorCombPositionField *pQryRCAMSInvestorCombPosition, int nRequestID) = 0;</p>
<span class="anchor" id="5b609dc8-9283-437a-8c78-d33c7886d6b8"></span>
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
<span class="anchor" id="6ddceeb8-658d-4d5a-9d09-556c6131d063"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="b1406766-6b6e-4ef9-830c-4c78c6c66d92"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="78d55c8f-47ab-47b9-92a0-2cdfb5fe0436"></span>
## 5.FAQ
<p>无</p>
