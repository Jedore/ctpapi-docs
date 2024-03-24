<p>请求查询二级代理操作员银期权限</p>
<p>响应: <a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYSECAGENTACIDMAP/">OnRspQrySecAgentACIDMap</a></p>
<span class="anchor" id="70694289-3f07-4a7e-b371-7cabd616cd7e"></span>
## 1.函数原型
<p>virtual int ReqQrySecAgentACIDMap(CThostFtdcQrySecAgentACIDMapField *pQrySecAgentACIDMap, int nRequestID) = 0;</p>
<span class="anchor" id="4185491d-05c1-43cf-8433-9d6b8500c6c7"></span>
## 2.参数
<p>pQrySecAgentACIDMap：二级代理操作员银期权限查询</p>
<table><tr><th style="TEXT-ALIGN: center;">字段类型</th><th style="TEXT-ALIGN: center;">字段名称</th><th style="TEXT-ALIGN: center;">含义</th><th style="TEXT-ALIGN: center;">是否可作为过滤条件</th></tr><tr><td style="TEXT-ALIGN: left;">TThostFtdcBrokerIDType</td>
<td style="TEXT-ALIGN: left;">BrokerID</td>
<td style="TEXT-ALIGN: left;">经纪公司代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcUserIDType</td>
<td style="TEXT-ALIGN: left;">UserID</td>
<td style="TEXT-ALIGN: left;">用户代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcAccountIDType</td>
<td style="TEXT-ALIGN: left;">AccountID</td>
<td style="TEXT-ALIGN: left;">资金账户</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcCurrencyIDType</td>
<td style="TEXT-ALIGN: left;">CurrencyID</td>
<td style="TEXT-ALIGN: left;">币种</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
</table>
<p>使用二级代理商操作员管理的投资者进行查询，字段值填写正确时，均无查询结果。</p>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="714a9202-6c28-41a5-9ebd-ad695b60ade9"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="afa6104c-8dce-49c3-8cad-957ca06d0875"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="00179340-bb96-415f-bd35-a583062fde6f"></span>
## 5.FAQ
<p>无</p>
