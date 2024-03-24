<p>请求RCAMS产品组合信息查询，对应响应请求<a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYRCAMSCOMBPRODUCTINFO/">OnRspQryRCAMSCombProductInfo</a></p>
<span class="anchor" id="dba009ee-636a-4746-955c-733203cd69af"></span>
## 1.函数原型
<p>virtual int ReqQryRCAMSCombProductInfo(CThostFtdcQryRCAMSCombProductInfoField *pQryRCAMSCombProductInfo, int nRequestID) = 0;</p>
<span class="anchor" id="86c79245-9c97-4c0e-9607-c5e96e93de91"></span>
## 2.参数
<p>pQryRCAMSCombProductInfo：RCAMS产品组合信息查询</p>
<table><tr><th style="TEXT-ALIGN: center;">字段类型</th><th style="TEXT-ALIGN: center;">字段名称</th><th style="TEXT-ALIGN: center;">含义</th><th style="TEXT-ALIGN: center;">是否可作为过滤条件</th></tr><tr><td style="TEXT-ALIGN: left;">TThostFtdcProductIDType</td>
<td style="TEXT-ALIGN: left;">ProductID</td>
<td style="TEXT-ALIGN: left;">产品代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcProductIDType</td>
<td style="TEXT-ALIGN: left;">CombProductID</td>
<td style="TEXT-ALIGN: left;">商品组代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcProductIDType</td>
<td style="TEXT-ALIGN: left;">ProductGroupID</td>
<td style="TEXT-ALIGN: left;">商品群代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
</table>
<span class="anchor" id="417d7a3e-e300-4a8b-9292-fa6542772221"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="2933f4ba-a37d-4c69-8cf4-25d0fc5a1143"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="6db945cc-3bcc-49fe-b180-b6fb7d79ddad"></span>
## 5.FAQ
<p>无</p>
