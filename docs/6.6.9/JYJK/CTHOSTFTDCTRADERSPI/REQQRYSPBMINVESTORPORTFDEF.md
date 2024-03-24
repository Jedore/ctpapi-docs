<p>请求投资者SPBM套餐选择查询，对应响应请求<a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYSPBMINVESTORPORTFDEF/">OnRspQrySPBMInvestorPortfDef</a></p>
<span class="anchor" id="6b168e3c-c06e-4c1d-ad19-20942dcba8c2"></span>
## 1.函数原型
<p>virtual int ReqQrySPBMInvestorPortfDef(CThostFtdcQrySPBMInvestorPortfDefField *pQrySPBMInvestorPortfDef, int nRequestID) = 0;</p>
<span class="anchor" id="b4b87650-843c-4c2d-9656-d76c38b134ff"></span>
## 2.参数
<p>pQrySPBMInvestorPortfDef：投资者套餐选择查询</p>
<pre><code>struct CThostFtdcQrySPBMInvestorPortfDefField
{
    ///交易所代码
    TThostFtdcExchangeIDType    ExchangeID;
    ///经纪公司代码
    TThostFtdcBrokerIDType  BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType    InvestorID;
};
</code></pre>
<table><tr><th style="TEXT-ALIGN: center;">字段类型</th><th style="TEXT-ALIGN: center;">字段名称</th><th style="TEXT-ALIGN: center;">含义</th><th style="TEXT-ALIGN: center;">是否可作为过滤条件</th></tr><tr><td style="TEXT-ALIGN: left;">TThostFtdcExchangeIDType</td>
<td style="TEXT-ALIGN: left;">ExchangeID</td>
<td style="TEXT-ALIGN: left;">交易所代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcBrokerIDType</td>
<td style="TEXT-ALIGN: left;">BrokerID</td>
<td style="TEXT-ALIGN: left;">经纪公司代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcInvestorIDType</td>
<td style="TEXT-ALIGN: left;">InvestorID</td>
<td style="TEXT-ALIGN: left;">投资者代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
</table>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="b9e7dea2-4c97-4e95-939e-0a465111d293"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="c7c7e786-7e4b-48bc-a0e0-4e71a5056240"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="ab7a6efb-b182-4770-9974-ae54ad495174"></span>
## 5.FAQ
<p>无</p>
