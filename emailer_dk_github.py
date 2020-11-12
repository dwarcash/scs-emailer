import smtplib
from smtplib import *
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from tabulate import tabulate

sender_email = ""
password = ""


receiver_email = ""


message = MIMEMultipart("alternative")
message["Subject"] = "Wishing you a very Happy Diwali 🎆"
message["From"] = sender_email
message["To"] = receiver_email

# Create the plain-text and HTML version of your message
text = """\
Hi,
Wishing you a very Happy Diwali !
Contact Us:
www.shreejicooling.com"""
html = """\
<!DOCTYPE html
	PUBLIC "-//W3C//DTD XHTML 1.0 Transitional //EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office"
	xmlns:v="urn:schemas-microsoft-com:vml">

<head>
	<!--[if gte mso 9]><xml><o:OfficeDocumentSettings><o:AllowPNG/><o:PixelsPerInch>96</o:PixelsPerInch></o:OfficeDocumentSettings></xml><![endif]-->
	<meta content="text/html; charset=utf-8" http-equiv="Content-Type" />
	<meta content="width=device-width" name="viewport" />
	<!--[if !mso]><!-->
	<meta content="IE=edge" http-equiv="X-UA-Compatible" />
	<!--<![endif]-->
	<title></title>
	<!--[if !mso]><!-->
	<link href="https://fonts.googleapis.com/css?family=Cabin" rel="stylesheet" type="text/css" />
	<link href="https://fonts.googleapis.com/css?family=Merriweather" rel="stylesheet" type="text/css" />
	<link href="https://fonts.googleapis.com/css?family=Oswald" rel="stylesheet" type="text/css" />
	<link href="https://fonts.googleapis.com/css?family=Oxygen" rel="stylesheet" type="text/css" />
	<!--<![endif]-->
	<style type="text/css">
		body {
			margin: 0;
			padding: 0;
			background-color: #161F33;
		}

		table,
		td,
		tr {
			vertical-align: top;
			border-collapse: collapse;
		}

		* {
			line-height: inherit;
		}

		a[x-apple-data-detectors=true] {
			color: inherit !important;
			text-decoration: none !important;
		}

		.footer-text {
			text-align: center;
			line-height: 1.2;
			font-family: 'Cabin', Arial, 'Helvetica Neue', Helvetica, sans-serif;
			word-break: break-word;
			mso-line-height-alt: 14px;
			margin: 0;
		}
	</style>
	<style id="media-query" type="text/css">
		@media (max-width: 670px) {

			.block-grid,
			.col {
				min-width: 320px !important;
				max-width: 100% !important;
				display: block !important;
			}

			.block-grid {
				width: 100% !important;
			}

			.col {
				width: 100% !important;
			}

			.col_cont {
				margin: 0 auto;
			}

			img.fullwidth,
			img.fullwidthOnMobile {
				max-width: 100% !important;
			}

			.no-stack .col {
				min-width: 0 !important;
				display: table-cell !important;
			}

			.no-stack.two-up .col {
				width: 50% !important;
			}

			.no-stack .col.num2 {
				width: 16.6% !important;
			}

			.no-stack .col.num3 {
				width: 25% !important;
			}

			.no-stack .col.num4 {
				width: 33% !important;
			}

			.no-stack .col.num5 {
				width: 41.6% !important;
			}

			.no-stack .col.num6 {
				width: 50% !important;
			}

			.no-stack .col.num7 {
				width: 58.3% !important;
			}

			.no-stack .col.num8 {
				width: 66.6% !important;
			}

			.no-stack .col.num9 {
				width: 75% !important;
			}

			.no-stack .col.num10 {
				width: 83.3% !important;
			}

			.video-block {
				max-width: none !important;
			}

			.mobile_hide {
				min-height: 0px;
				max-height: 0px;
				max-width: 0px;
				display: none;
				overflow: hidden;
				font-size: 0px;
			}

			.desktop_hide {
				display: block !important;
				max-height: none !important;
			}
		}
	</style>
	<style id="menu-media-query" type="text/css">
		@media (max-width: 670px) {
			.menu-checkbox[type="checkbox"]~.menu-links {
				display: none !important;
				padding: 5px 0;
			}

			.menu-checkbox[type="checkbox"]~.menu-links span.sep {
				display: none;
			}

			.menu-checkbox[type="checkbox"]:checked~.menu-links,
			.menu-checkbox[type="checkbox"]~.menu-trigger {
				display: block !important;
				max-width: none !important;
				max-height: none !important;
				font-size: inherit !important;
			}

			.menu-checkbox[type="checkbox"]~.menu-links>a,
			.menu-checkbox[type="checkbox"]~.menu-links>span.label {
				display: block !important;
				text-align: center;
			}

			.menu-checkbox[type="checkbox"]:checked~.menu-trigger .menu-close {
				display: block !important;
			}

			.menu-checkbox[type="checkbox"]:checked~.menu-trigger .menu-open {
				display: none !important;
			}

			#menump28ct~div label {
				border-radius: 0% !important;
			}

			#menump28ct:checked~.menu-links {
				background-color: transparent !important;
			}

			#menump28ct:checked~.menu-links a {
				color: #6bc5ff !important;
			}

			#menump28ct:checked~.menu-links span {
				color: #6bc5ff !important;
			}
		}
	</style>
	<style id="icon-media-query" type="text/css">
		@media (max-width: 670px) {
			.icons-inner {
				text-align: center;
			}

			.icons-inner td {
				margin: 0 auto;
			}
		}
	</style>
</head>

<body class="clean-body" style="margin: 0; 
padding: 0; 
-webkit-text-size-adjust: 100%; 
background-color: #FFFFFF;">
	<table bgcolor="#FFFFFF" cellpadding="0" cellspacing="0" class="nl-container" role="presentation" style="table-layout: fixed; 
		vertical-align: top; 
		min-width: 320px; 
		border-spacing: 0; 
		border-collapse: collapse; 
		mso-table-lspace: 0pt; 
		mso-table-rspace: 0pt; 
		background-color: #FFFFFF; 
		width: 100%;" valign="top" width="100%">
		<tbody>
			<tr style="vertical-align: top;" valign="top">
				<td style="word-break: break-word; vertical-align: top;" valign="top">
					<div style="background-color:transparent;">
						<div class="block-grid mixed-two-up"
							style="min-width: 320px; max-width: 650px; overflow-wrap: break-word; word-wrap: break-word; word-break: break-word; margin: 0 auto; background-color: #161F33;">
							<div style="border-collapse: collapse;display: table;width: 100%;background-color:#161F33;">
								<div class="col num4"
									style="display: table-cell; vertical-align: top; max-width: 320px; min-width: 216px; width: 216px;">
									<div class="col_cont" style="width:100% !important;">
										<div style="border-top:0px solid transparent; 
											border-left:0px solid transparent; 
											border-bottom:0px solid transparent; 
											border-right:0px solid transparent; 
											padding-top:5px; 
											padding-bottom:5px; 
											padding-right: 0px; 
											padding-left: 0px;">
											<div align="center" class="img-container center fixedwidth"
												style="padding-right: 0px;padding-left: 10px;">
												<a href="https://shreejicooling.com" style="outline:none" tabindex="-1"
													target="_blank"> <img align="center"
														alt="scs shreeji cooling hvac inverter best hvac consutancy ac supplier vrf hvac system sreejicooling trunkey scs"
														border="0" class="center fixedwidth"
														src="https://firebasestorage.googleapis.com/v0/b/crime-record-app.appspot.com/o/shreeji%2Fcompressed%2Flogos%2FShreeji_no_iso_lowres.png?alt=media&token=1d1a1c78-3463-433b-a5a1-82b7a3387feb"
														style="text-decoration: none; -ms-interpolation-mode: bicubic; height: auto; border: 0; width: 100%; max-width: 173px; display: block;"
														title="SCS - Shreeji Coolling System" width="173" /></a>
											</div>
										</div>
									</div>
								</div>
								<div class="col num8" style="display: table-cell; 
									vertical-align: top; 
									min-width: 320px; 
									max-width: 432px; 
									width: 433px;">
									<div class="col_cont" style="width:100% !important;">
										<div style="border-top:0px solid transparent; 
											border-left:0px solid transparent; 
											border-bottom:0px solid transparent; 
											border-right:0px solid transparent; 
											padding-top:20px; 
											padding-bottom:20px; 
											padding-right: 20px; 
											padding-left: 20px;">
											<table border="0" cellpadding="0" cellspacing="0" role="presentation"
												style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt;"
												valign="top" width="100%">
												<tr style="vertical-align: top;" valign="top">
													<td align="center" style="word-break: break-word; 
														vertical-align: top; 
														padding-top: 0px; 
														padding-bottom: 0px; 
														padding-left: 0px; 
														padding-right: 0px; 
														text-align: center; 
														font-size: 0px;" valign="top">
														<div class="menu-links">
															<a href="https://shreejicooling.com/projects/" style="padding-top:0px;
																padding-bottom:0px;
																padding-left:15px;
																padding-right:15px;
																display:inline;
																color:#d1edff;
																font-family:'Cabin', Arial, 'Helvetica Neue', Helvetica, sans-serif;
																font-size:14px;
																text-decoration:none;">PROJECTS</a>
															<span class="sep" style="font-size:14px;
																font-family:'Cabin', Arial, 'Helvetica Neue', Helvetica, sans-serif;
																color:#000000;">|</span>
															<a href="https://shreejicooling.com/service/"
																style="padding-top:0px;padding-bottom:0px;padding-left:15px;padding-right:15px;display:inline;color:#d1edff;font-family:'Cabin', Arial, 'Helvetica Neue', Helvetica, sans-serif;font-size:14px;text-decoration:none;">SERVICES</a>
															<span class="sep"
																style="font-size:14px;font-family:'Cabin', Arial, 'Helvetica Neue', Helvetica, sans-serif;color:#000000;">|</span>
															<a href="tel:02612547254"
																style="padding-top:0px;padding-bottom:0px;padding-left:15px;padding-right:15px;display:inline;color:#d1edff;font-family:'Cabin', Arial, 'Helvetica Neue', Helvetica, sans-serif;font-size:14px;text-decoration:none;">CONTACT</a>

														</div>
													</td>
												</tr>
											</table>

										</div>

									</div>
								</div>

							</div>
						</div>
					</div>

					<hr style="max-width:650px;margin-top:0px;margin-bottom:0px;border: 0px; height:0.5px;background-color: 
					#263b4a;">

					<div style="background-color:transparent;">
						<div class="block-grid"
							style="min-width: 320px; max-width: 650px; overflow-wrap: break-word; word-wrap: break-word; word-break: break-word; Margin: 0 auto; background-color: #161F33;">
							<div style="border-collapse: collapse;display: table;width: 100%;background-color:#161F33;">

								<div class="col num12"
									style="min-width: 320px; max-width: 650px; display: table-cell; vertical-align: top; width: 650px;">
									<div class="col_cont" style="width:100% !important;">

										<div
											style="border-top:0px solid transparent; border-left:0px solid transparent; border-bottom:0px solid transparent; border-right:0px solid transparent; padding-top:10px; padding-bottom:0px; padding-right: 0px; padding-left: 0px;">

											<div
												style="color:#393d47;font-family:'Cabin', Arial, 'Helvetica Neue', Helvetica, sans-serif;line-height:1.2;padding-top:10px;padding-right:20px;padding-bottom:10px;padding-left:20px;">
												<div
													style="line-height: 1.2; font-size: 12px; font-family: 'Cabin', Arial, 'Helvetica Neue', Helvetica, sans-serif; color: #393d47; mso-line-height-alt: 14px;">
													<p
														style="font-size: 24px; line-height: 1.2; word-break: break-word; text-align: center; font-family: 'Cabin', Arial, 'Helvetica Neue', Helvetica, sans-serif; mso-line-height-alt: 29px; margin: 0;">
														<span style="color: #6bc5ff; font-size: 24px;"><strong>Wishing
																you a safe and Happy Diwali !</strong></span></p>
												</div>
											</div>

										</div>

									</div>
								</div>

							</div>
						</div>
					</div>
					<div style="background-color:transparent;">
						<div class="block-grid"
							style="min-width: 320px; max-width: 650px; overflow-wrap: break-word; word-wrap: break-word; word-break: break-word; margin: 0 auto; background-color: #161F33;">
							<div style="border-collapse: collapse;display: table;width: 100%;background-color:#161F33;">
								<div class="col num12"
									style="min-width: 320px; max-width: 650px; display: table-cell; vertical-align: top; width: 650px;">
									<div class="col_cont" style="width:100% !important; border: px solid;">
										<div
											style="border-top:0px solid transparent; border-left:0px solid transparent; border-bottom:0px solid transparent; border-right:0px solid transparent; padding:0px">
											<div align="center" class="img-container center autowidth" style="padding-right: 0px;
												padding-left: 0px;
												padding-top: 0px;
												">
												<p></p>
												<a href="https://shreejicooling.com">
													<img align="center"
														alt="scs shreeji cooling hvac inverter best hvac consutancy ac supplier vrf hvac system sreejicooling trunkey scs"
														border="0" class="center autowidth"
														src="https://firebasestorage.googleapis.com/v0/b/crime-record-app.appspot.com/o/shreeji%2Fgifs%2Fdiwali_email%20(3).gif?alt=media&token=19e5c6b7-86f9-4547-809a-c506cd930591"
														style="text-decoration: none; -ms-interpolation-mode: bicubic; height: auto; border: 0; width: 100%; max-width: 650px; display: block;"
														title="SCS - India's Leading HVAC Consultancy"
														width="650px" /></a>
											</div>
										</div>
									</div>
								</div>
							</div>
						</div>
					</div>
					<div style="background-color:transparent;">
						<div class="block-grid"
							style="min-width: 320px; max-width: 650px; overflow-wrap: break-word; word-wrap: break-word; word-break: break-word; Margin: 0 auto; background-color: #161F33;">
							<div style="border-collapse: collapse;display: table;width: 100%;background-color:#161F33;">

								<div class="col num12"
									style="min-width: 320px; max-width: 650px; display: table-cell; vertical-align: top; width: 650px;">
									<div class="col_cont" style="width:100% !important;">

										<div
											style="border-top:0px solid transparent; border-left:0px solid transparent; border-bottom:0px solid transparent; border-right:0px solid transparent; padding-top:0px; padding-bottom:5px; padding-right: 0px; padding-left: 0px;">

											<div
												style="color:#393d47;font-family:Arial, Helvetica Neue, Helvetica, sans-serif;line-height:1.5;padding-top:10px;padding-right:45px;padding-bottom:10px;padding-left:45px;">
												<div
													style="line-height: 1.5; font-size: 12px; color: #393d47; font-family: Arial, Helvetica Neue, Helvetica, sans-serif; mso-line-height-alt: 18px;">
													<p
														style="font-size: 14px; line-height: 1.5; word-break: break-word; text-align: center; mso-line-height-alt: 21px; margin: 0;">
														<span style="color: #d1edff;">
															<table style="margin: 0px auto;">

																<tr>

																	<td style="padding-left:5px;padding-bottom:0px">
																		<h2
																			style="color: #d1edff; margin:0px auto;text-align:center;">
																			Wishing you a very Happy Diwali.<br>As we
																			celebrate Diwali 2020, let's hope that it
																			brings us new opportunities to work together
																			and prosper.</h2>
																	</td>

																</tr>
															</table>

														</span>
													</p>
												</div>
											</div>

										</div>

									</div>
								</div>

							</div>
						</div>
					</div>
					<div style="background-color:transparent;">
						<div class="block-grid two-up no-stack"
							style="min-width: 320px; max-width: 650px; overflow-wrap: break-word; word-wrap: break-word; word-break: break-word; Margin: 0 auto; background-color: #161F33;">
							<div style="border-collapse: collapse;display: table;width: 100%;background-color:#161F33;">

								<div class="col num6"
									style="display: table-cell; vertical-align: top; max-width: 320px; min-width: 324px; width: 325px;">

									<div class="col_cont" style="width:100% !important;">


										<div
											style="border-top:0px solid transparent; border-left:0px solid transparent; border-bottom:0px solid transparent; border-right:0px solid transparent; padding-top:0px; padding-bottom:0px; padding-right: 0px; padding-left: 0px; margin-bottom:15px">

											<div align="center" class="button-container"
												style="padding-top:0px;padding-right:25px;padding-bottom:15px;padding-left:10px;">

												<div style="text-decoration:none;
													display:inline-block;
													color:#ffffff;
													background-color:#0D73B5;
													border-radius:4px;
													-webkit-border-radius:4px;
													-moz-border-radius:4px;
													width:auto; width:auto;
													border-top:0px solid #0d73b5;
													border-right:0px solid #0d73b5;
													border-bottom:0px solid #0d73b5;
													border-left:0px solid #0d73b5;
													padding-top:5px;
													padding-bottom:5px;
													font-family:'Cabin', Arial, 'Helvetica Neue', Helvetica, sans-serif;text-align:center;
													mso-border-alt:none;
													word-break:keep-all;">
													<a style="color: white;" href="https://shreejicooling.com">
														<span style="padding-left:20px;
															padding-right:20px;
															font-size:16px;
															display:inline-block;">
															<span style="font-size: 16px;
															text-align:center;
																line-height: 2;
																word-break: break-word;
																font-family: 'Cabin', Arial, 'Helvetica Neue', Helvetica, sans-serif;
																mso-line-height-alt: 32px;">About Us
															</span>
														</span>
													</a>
												</div>
											</div>
										</div>
									</div>
								</div>
							</div>
						</div>
						<div style="background-color:transparent;">
							<div class="block-grid"
								style="min-width: 320px; max-width: 650px; overflow-wrap: break-word; word-wrap: break-word; word-break: break-word; margin: 0 auto; background-color: #161F33;">
								<div
									style="border-collapse: collapse;display: table;width: 100%;background-color:#161F33;">
									<div class="col num12"
										style="min-width: 320px; max-width: 650px; display: table-cell; vertical-align: top; width: 650px;">
										<div class="col_cont" style="width:100% !important; border: px solid;">
											<div
												style="border-top:0px solid transparent; border-left:0px solid transparent; border-bottom:0px solid transparent; border-right:0px solid transparent; padding:0px">
												<div align="center" class="img-container center autowidth" style="padding-right: 0px;
													padding-left: 0px;
													padding-top: 0px;
													position: relative;
													"><a href="https://shreejicooling.com">
														<img align="center"
															alt="scs shreeji cooling hvac inverter best hvac consutancy ac supplier vrf hvac system sreejicooling trunkey scs"
															border="0" class="center autowidth"
															src="https://firebasestorage.googleapis.com/v0/b/crime-record-app.appspot.com/o/shreeji%2Femail_header.png?alt=media&token=e958cf1d-b43d-44dc-9eab-8bdd11e53d20"
															style="text-decoration: none; -ms-interpolation-mode: bicubic; height: auto; border: 0; width: 100%; max-width: 650px; display: block;"
															title="SCS - Shreeji Cooling System" width="650px" /></a>
													<!-- <a href="https://shreejicooling.com"
														title="SCS - Shreeji Cooling System" style="outline:none"
														tabindex="-1" target="_blank">
														<div
															style="position: absolute; left: 1%; top: 5%; width: 33%; height: 52%; background-color: transparent;">
														</div>
													</a>
													<a href="https://www.bluestraindia.com" title="SCS - Bluestar"
														style="outline:none" tabindex="-1" target="_blank">
														<div
															style="position: absolute; right: 1%; top: 5%; width: 33%; height: 52%; background-color: transparent;">
														</div>
													</a>
													<a href="mailto:info@shreejicooling.com" title="SCS - Email"
														style="outline:none" tabindex="-1" target="_blank">
														<div
															style="position: absolute; right: 3%; bottom: 5%; width: 33%; height: 27%; background-color: transparent;">
														</div>
													</a>
													<a href="tel:+91 02612547254" title="SCS - Contact"
														style="outline:none" tabindex="-1" target="_blank">
														<div
															style="position: absolute; right: 39%; bottom: 5%; width: 23%; height: 27%; background-color: transparent;">
														</div>
													</a>
													<a href="https://shreejicooling.com" title="SCS - Website"
														style="outline:none" tabindex="-1" target="_blank">
														<div
															style="position: absolute; left: 2%; bottom: 5%; width: 32%; height: 27%; background-color: transparent;">
														</div>
													</a> -->
												</div>
											</div>
										</div>
									</div>
								</div>
							</div>
						</div>
						<div style="background-color:transparent;">
							<div class="block-grid"
								style="min-width: 320px; max-width: 650px; overflow-wrap: break-word; word-wrap: break-word; word-break: break-word; Margin: 0 auto; background-color: transparent;">
								<div
									style="border-collapse: collapse;display: table;width: 100%;background-color:transparent;">

									<div class="col num12"
										style="min-width: 320px; max-width: 650px; display: table-cell; vertical-align: top; width: 648px;">
										<div class="col_cont" style="width:100% !important;">

											<div
												style="border-top:1px solid #EFEFEF; border-left:1px solid #EFEFEF; border-bottom:1px solid #EFEFEF; border-right:1px solid #EFEFEF; padding-top:5px; padding-bottom:5px; padding-right: 0px; padding-left: 0px;">

												<table cellpadding="0" cellspacing="0" class="social_icons"
													role="presentation"
													style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt;"
													valign="top" width="100%">
													<tbody>
														<tr style="vertical-align: top;" valign="top">
															<td style="word-break: break-word; vertical-align: top; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px;"
																valign="top">
																<table align="center" cellpadding="0" cellspacing="0"
																	class="social_table" role="presentation"
																	style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; mso-table-tspace: 0; mso-table-rspace: 0; mso-table-bspace: 0; mso-table-lspace: 0;"
																	valign="top">
																	<tbody>
																		<tr align="center"
																			style="vertical-align: top; display: inline-block; text-align: center;"
																			valign="top">
																			<td style="word-break: break-word; vertical-align: top; padding-bottom: 0; padding-right: 2.5px; padding-left: 2.5px;"
																				valign="top"><a
																					href="https://www.facebook.com/shreejicoolingsystem"
																					target="_blank"><img alt="Facebook"
																						height="32"
																						src="https://firebasestorage.googleapis.com/v0/b/crime-record-app.appspot.com/o/shreeji%2Fsocial%20icons%2Ffacebook2x.png?alt=media&token=0bfa3354-7b1b-444e-9faf-56c0494c1121"
																						style="text-decoration: none; -ms-interpolation-mode: bicubic; height: auto; border: 0; display: block;"
																						title="facebook"
																						width="32" /></a>
																			</td>
																			<td style="word-break: break-word; vertical-align: top; padding-bottom: 0; padding-right: 2.5px; padding-left: 2.5px;"
																				valign="top"><a
																					href="https://www.linkedin.com/company/shreeji-cooling-system"
																					target="_blank"><img alt="Linkedin"
																						height="32"
																						src="https://firebasestorage.googleapis.com/v0/b/crime-record-app.appspot.com/o/shreeji%2Fsocial%20icons%2Flinkedin2x.png?alt=media&token=61a66d77-391f-4318-9448-4eca3de07131"
																						style="text-decoration: none; -ms-interpolation-mode: bicubic; height: auto; border: 0; display: block;"
																						title="linkedin"
																						width="32" /></a>
																			</td>
																			<td style="word-break: break-word; vertical-align: top; padding-bottom: 0; padding-right: 2.5px; padding-left: 2.5px;"
																				valign="top"><a
																					href="https://www.instagram.com/shreejicooling"
																					target="_blank"><img alt="Instagram"
																						height="32"
																						src="https://firebasestorage.googleapis.com/v0/b/crime-record-app.appspot.com/o/shreeji%2Fsocial%20icons%2Finstagram2x.png?alt=media&token=90a988b1-4dc6-4922-a0c8-089663ba9d3b"
																						style="text-decoration: none; -ms-interpolation-mode: bicubic; height: auto; border: 0; display: block;"
																						title="instagram"
																						width="32" /></a>
																			</td>
																			<td style="word-break: break-word; vertical-align: top; padding-bottom: 0; padding-right: 2.5px; padding-left: 2.5px;"
																				valign="top"><a
																					href="https://www.twitter.com/shreeji_cooling"
																					target="_blank"><img alt="Twitter"
																						height="32"
																						src="https://firebasestorage.googleapis.com/v0/b/crime-record-app.appspot.com/o/shreeji%2Fsocial%20icons%2Ftwitter2x.png?alt=media&token=74d350f4-24ef-4573-b9ae-f9c1b39d44ac"
																						style="text-decoration: none; -ms-interpolation-mode: bicubic; height: auto; border: 0; display: block;"
																						title="twitter"
																						width="32" /></a>
																			</td>
																		</tr>
																	</tbody>
																</table>
															</td>
														</tr>
													</tbody>
												</table>

												<table border="0" cellpadding="0" cellspacing="0" class="divider"
													role="presentation"
													style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; min-width: 100%; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;"
													valign="top" width="100%">
													<tbody>
														<tr style="vertical-align: top;" valign="top">
															<td class="divider_inner"
																style="word-break: break-word; vertical-align: top; min-width: 100%; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; padding-top: 10px; padding-right: 10px; padding-bottom: 10px; padding-left: 10px;"
																valign="top">
																<table align="center" border="0" cellpadding="0"
																	cellspacing="0" class="divider_content"
																	role="presentation"
																	style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; border-top: 1px solid #EFEFEF; width: 80%;"
																	valign="top" width="80%">
																	<tbody>
																		<tr style="vertical-align: top;" valign="top">
																			<td style="word-break: break-word; vertical-align: top; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;"
																				valign="top"><span></span></td>
																		</tr>
																	</tbody>
																</table>
															</td>
														</tr>
													</tbody>
												</table>

												<div
													style="color:#393d47;font-family:'Cabin', Arial, 'Helvetica Neue', Helvetica, sans-serif;line-height:1.2;padding-top:10px;padding-right:10px;padding-bottom:10px;padding-left:10px;">
													<div
														style="line-height: 1.2; font-size: 12px; font-family: 'Cabin', Arial, 'Helvetica Neue', Helvetica, sans-serif; color: #444444; mso-line-height-alt: 14px;">
														<p
															style="text-align: center; line-height: 1.2; font-family: 'Cabin', Arial, 'Helvetica Neue', Helvetica, sans-serif; word-break: break-word; mso-line-height-alt: 14px; margin: 0;">
															Shreeji Cooling System | 3021, CENTRAL BAZZAR, opp. Varachha
															Main Road,
															<br>Surat, Gujarat - 395006<br>
															<br>India's Leading HVAC Consultancy
														</p>
														<br>

														<p class="footer-text">
															<a href="https://shreejicooling.com" rel="noopener"
																style="text-decoration: none; color: #0d73b5;"
																target="_blank">www.shreejicooling.com</a> -<a
																href="mailto:info@shreejicooling.com" rel="noopener"
																style="text-decoration: none; color: #0d73b5;"
																target="_blank" title="Mail"> info@shreejicoolng.com</a>
															-
															<a href="tel:02612547254" rel="noopener"
																style="text-decoration: none; color: #0d73b5;"
																target="_blank" title="Phone">0261-2547254</a></p>
														<br>
														<p class="footer-text">
															©2020 Shreeji Cooling System. All rights reserved.</p>
													</div>
												</div>
											</div>
										</div>
									</div>
								</div>
							</div>
						</div>
				</td>
			</tr>
		</tbody>
	</table>
</body>

</html>
"""

# Turn these into plain/html MIMEText objects
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part1)
message.attach(part2)

# Create secure connection with server and send email
try:
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )
        status = "✅"
        error = "None"
except SMTPResponseException as e:
    print("Error: unable to send email")
    error_code = e.smtp_code
    error_message = e.smtp_error
    if (error_code == 422):
        error = "Recipient Mailbox Full"
    elif(error_code == 431):
        error = "Server out of space"
    elif(error_code == 447):
        error = "Timeout. Try reducing number of recipients"
    elif(error_code == 510 or error_code == 511):
        error = "One of the addresses in your TO, CC or BBC line doesn't exist. Check again your recipients' accounts and correct any possible misspelling."
    elif(error_code == 512):
        error = "Check again all your recipients' addresses: there will likely be an error in a domain name (like mail@domain.coom instead of mail@domain.com)"
    elif(error_code == 535):
        error = "Username or password incorrect!"
    elif(error_code == 541 or error_code == 554):
        error = "Your message has been detected and labeled as spam. You must ask the recipient to whitelist you"
    elif(error_code == 550):
        error = "Though it can be returned also by the recipient's firewall (or when the incoming server is down), the great majority of errors 550 simply tell that the recipient email address doesn't exist. You should contact the recipient otherwise and get the right address."
    elif(error_code == 553):
        error = "Check all the addresses in the TO, CC and BCC field. There should be an error or a misspelling somewhere."
    else:
        print("Error code: ")
        print(error_code)
        print("Error Message: ")
        print(error_message)
        error = error_message
    status = "❌"


table = [["Email From:", "Email To: ", "Delivered", "Error"],
         [sender_email, receiver_email, status, error]]
output = tabulate(table, tablefmt='grid')

print(output)
