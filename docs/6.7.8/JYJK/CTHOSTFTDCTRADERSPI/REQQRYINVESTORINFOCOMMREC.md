<p>投资者申报费阶梯收取记录查询，对应响应请求<a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYINVESTORINFOCOMMREC/">OnRspQryInvestorInfoCommRec</a></p>
<p>请求查询时3个入参都支持为空，查询期权系列的申报费时通过填写标的的商品代码查询。同一个投资者、同一个商品代码可能会返回两条记录：</p>
<p>一条记录为期货合约的申报费收取记录，IsOptSeries字段返回为0；</p>
<p>一条记录为以此期货合约为标的的系列期权的申报费收取记录，IsOptSeries字段返回为1。</p>
<span class="anchor" id="7d55018b-cc7f-4c8a-9fb8-5568cf060349"></span>
## 1.函数原型
<p>virtual int <a href="../REQQRYINVESTORPORTFSETTING/">ReqQryInvestorPortfSetting</a>(CThostFtdcQryInvestorPortfSettingField *pQryInvestorPortfSetting, int nRequestID) = 0;</p>
<span class="anchor" id="1f77d011-fea5-4f43-b9e4-f95ea72b3941"></span>
## 2.参数
<p>pQryInvestorPortfSetting：投资者申报费阶梯收取记录查询</p>
<table><tr><th style="TEXT-ALIGN: center;">字段类型</th><th style="TEXT-ALIGN: center;">字段名称</th><th style="TEXT-ALIGN: center;">含义</th><th style="TEXT-ALIGN: center;">是否可作为过滤条件</th></tr><tr><td style="TEXT-ALIGN: left;">TThostFtdcInstrumentIDType</td>
<td style="TEXT-ALIGN: left;">InstrumentID</td>
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
<span class="anchor" id="d5f6d23d-1d0c-4f0e-9fea-a7b943b2541d"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="37762391-1781-4acb-b61f-9e959d549c7d"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="00ebcf0e-b389-442d-9b77-d1bc2b4fb266"></span>
## 5.FAQ
<p>无</p>
