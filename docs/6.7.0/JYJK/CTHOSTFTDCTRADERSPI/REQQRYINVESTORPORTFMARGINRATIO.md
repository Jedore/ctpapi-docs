<p>请求投资者新型组合保证金系数查询，对应响应请求<a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYINVESTORPORTFMARGINRATIO/">OnRspQryInvestorPortfMarginRatio</a></p>
<span class="anchor" id="6c6b424c-8ef0-4cb7-8a6a-712a3e5bb7ec"></span>
## 1.函数原型
<p>virtual int ReqQryInvestorPortfMarginRatio(CThostFtdcQryInvestorPortfMarginRatioField *pQryInvestorPortfMarginRatio, int nRequestID) = 0;</p>
<span class="anchor" id="a71e2076-36da-4e81-9f80-9af036937722"></span>
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
<span class="anchor" id="cde84038-5237-4b19-ac79-55bd232c2015"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="35646ef5-3f78-44c9-81d6-2d395e28c995"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="e58cecb2-2971-4bc1-8185-c69ca6b84833"></span>
## 5.FAQ
<p>无</p>
