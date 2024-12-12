<p>投资者新型组合保证金开关查询，对应响应请求<a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYINVESTORPORTFSETTING/">OnRspQryInvestorPortfSetting</a></p>
<span class="anchor" id="d6a52464-9070-498b-a968-ed9ab4e2ad04"></span>
## 1.函数原型
<p>virtual int ReqQryInvestorPortfSetting(CThostFtdcQryInvestorPortfSettingField *pQryInvestorPortfSetting, int nRequestID) = 0;</p>
<span class="anchor" id="aff81c3b-1046-4642-9741-38cdb550edc7"></span>
## 2.参数
<p>pQryInvestorPortfSetting：投资者新组保设置查询</p>
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
<span class="anchor" id="e468d3c8-d5c3-4955-aa14-a4e2fa09d44a"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="c3490b08-9ef8-4da3-a341-eb26ddf7d44d"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="bb585460-b2d5-46b3-a70c-0ab36ee4edb3"></span>
## 5.FAQ
<p>无</p>
