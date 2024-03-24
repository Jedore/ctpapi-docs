<p>请求RULE跨品种抵扣参数查询，对应响应请求<a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYRULEINTERPARAMETER/">OnRspQryRULEInterParameter</a></p>
<span class="anchor" id="627edb1a-94d6-4d18-89ba-8d07a1158bcc"></span>
## 1.函数原型
<p>virtual int ReqQryRULEInterParameter(CThostFtdcQryRULEInterParameterField *pQryRULEInterParameter, int nRequestID) = 0;</p>
<span class="anchor" id="37f7eb3f-3d3e-427b-88ef-583625877da0"></span>
## 2.参数
<p>pQryRULEInterParameter：RULE跨品种抵扣参数查询</p>
<table><tr><th style="TEXT-ALIGN: center;">字段类型</th><th style="TEXT-ALIGN: center;">字段名称</th><th style="TEXT-ALIGN: center;">含义</th><th style="TEXT-ALIGN: center;">是否可作为过滤条件</th></tr><tr><td style="TEXT-ALIGN: left;">TThostFtdcExchangeIDType</td>
<td style="TEXT-ALIGN: left;">ExchangeID</td>
<td style="TEXT-ALIGN: left;">交易所代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcInstrumentIDType</td>
<td style="TEXT-ALIGN: left;">Leg1ProdFamilyCode</td>
<td style="TEXT-ALIGN: left;">第一腿构成品种</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcInstrumentIDType</td>
<td style="TEXT-ALIGN: left;">Leg1ProdFamilyCode</td>
<td style="TEXT-ALIGN: left;">第二腿构成品种</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcCommodityGroupIDType</td>
<td style="TEXT-ALIGN: left;">CommodityGroupID</td>
<td style="TEXT-ALIGN: left;">商品群号</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
</table>
<span class="anchor" id="e86cabe3-f76b-4ac2-ae8b-33f2cf23b64f"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="69753704-2e30-4078-95ca-894338907631"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="91698e4e-e08f-48b7-b921-18173db0ce7e"></span>
## 5.FAQ
<p>无</p>
