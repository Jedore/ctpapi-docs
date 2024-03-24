<p>请求投资者新型组合保证金系数查询，对应响应请求<a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYINVESTORPORTFMARGINRATIO/">OnRspQryInvestorPortfMarginRatio</a></p>
<span class="anchor" id="8d47f6bd-0303-4403-b045-fb3a6829a354"></span>
## 1.函数原型
<p>virtual int ReqQryInvestorPortfMarginRatio(CThostFtdcQryInvestorPortfMarginRatioField *pQryInvestorPortfMarginRatio, int nRequestID) = 0;</p>
<span class="anchor" id="d677f967-d6d0-4c60-9d0b-5c177898be5e"></span>
## 2.参数
<p>pQryInvestorPortfMarginRatio：投资者新型组合保证金系数查询</p>
<pre><code>struct CThostFtdcQryInvestorPortfMarginRatioField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType  BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType    InvestorID;
    ///交易所代码
    TThostFtdcExchangeIDType    ExchangeID;
};
</code></pre>
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
<tr><td style="TEXT-ALIGN: left;">TThostFtdcExchangeIDType</td>
<td style="TEXT-ALIGN: left;">ExchangeID</td>
<td style="TEXT-ALIGN: left;">交易所代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
</table>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="33e33eec-933b-4682-a1fd-b24d17157da3"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="6d339450-dccd-4cb3-ac86-10e0fc5db5fb"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="87ed765f-cb82-4ae6-b19b-eb5defeab9a6"></span>
## 5.FAQ
<p>无</p>
